import pytest

from task_manager.application.complete_task import CompleteTaskUseCase
from task_manager.application.create_task import CreateTaskUseCase
from task_manager.domain.enums import TaskStatus


def test_should_create_task_with_pending_status() -> None:
    use_case = CreateTaskUseCase()

    task = use_case.execute(
        title="Learn DDD",
        description="Study clean architecture",
    )

    assert task.title == "Learn DDD"
    assert task.description == "Study clean architecture"
    assert task.status == TaskStatus.PENDING


def test_should_complete_task_successfully() -> None:
    task = CreateTaskUseCase().execute(
        title="Learn DDD",
        description="Study clean architecture",
    )

    use_case = CompleteTaskUseCase()

    updated_task = use_case.execute(task)

    assert updated_task.status == TaskStatus.COMPLETED


def test_should_not_complete_task_twice() -> None:
    task = CreateTaskUseCase().execute(
        title="Learn Python",
        description="OOP practice",
    )

    use_case = CompleteTaskUseCase()

    use_case.execute(task)

    with pytest.raises(ValueError):
        use_case.execute(task)
