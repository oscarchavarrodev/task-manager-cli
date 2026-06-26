import pytest

from task_manager.domain.enums import TaskStatus


def test_should_create_task_using_sqlite_repository(
    create_use_case,
    repository,
) -> None:
    task = create_use_case.execute(
        title="Learn Clean Architecture",
        description="Integration test",
    )

    saved_task = repository.get_by_id(task.id)

    assert saved_task is not None
    assert saved_task.id == task.id
    assert saved_task.title == task.title


def test_should_complete_task_using_sqlite_repository(
    create_use_case,
    complete_use_case,
    repository,
) -> None:
    task = create_use_case.execute(
        title="Learn SQLite",
        description="Integration test for completing a task",
    )

    complete_use_case.execute(task.id)

    saved_task = repository.get_by_id(task.id)

    assert saved_task is not None
    assert saved_task.status == TaskStatus.COMPLETED


def test_should_delete_task_using_sqlite_repository(
    create_use_case,
    delete_use_case,
    repository,
) -> None:
    task = create_use_case.execute(
        title="Delete me",
        description="Temporary task",
    )

    delete_use_case.execute(task.id)

    deleted_task = repository.get_by_id(task.id)

    assert deleted_task is None


def test_should_get_task_using_sqlite_repository(
    create_use_case,
    get_use_case,
) -> None:
    task = create_use_case.execute(
        title="Learn SQLite",
        description="Get task integration test",
    )

    found_task = get_use_case.execute(task.id)

    assert found_task.id == task.id
    assert found_task.title == task.title
    assert found_task.description == task.description


def test_should_get_all_tasks_using_sqlite_repository(
    create_use_case,
    repository,
) -> None:
    task1 = create_use_case.execute(
        title="Task 1",
        description="First task",
    )

    task2 = create_use_case.execute(
        title="Task 2",
        description="Second task",
    )

    tasks = repository.get_all()

    task_ids = [task.id for task in tasks]

    assert task1.id in task_ids
    assert task2.id in task_ids


def test_should_not_delete_completed_task_using_sqlite_repository(
    create_use_case,
    complete_use_case,
    delete_use_case,
) -> None:
    task = create_use_case.execute(
        title="Protected task",
        description="Cannot be deleted",
    )

    complete_use_case.execute(task.id)

    with pytest.raises(ValueError, match="Cannot delete completed task"):
        delete_use_case.execute(task.id)
