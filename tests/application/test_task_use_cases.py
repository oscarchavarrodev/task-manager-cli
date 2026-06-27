import pytest

from task_manager.domain.enums import TaskStatus

# =========================
# CREATE TASK
# =========================


def test_should_create_task_with_pending_status(create_use_case) -> None:
    task = create_use_case.execute(
        title="Learn DDD",
        description="Study clean architecture",
    )

    assert task.title == "Learn DDD"
    assert task.description == "Study clean architecture"
    assert task.status == TaskStatus.PENDING


# =========================
# COMPLETE TASK
# =========================


def test_should_complete_task_successfully(create_use_case, complete_use_case) -> None:
    task = create_use_case.execute(
        title="Learn DDD",
        description="Study clean architecture",
    )

    updated_task = complete_use_case.execute(task.id)

    assert updated_task.status == TaskStatus.COMPLETED


def test_should_not_complete_task_twice(create_use_case, complete_use_case) -> None:
    task = create_use_case.execute(
        title="Learn Python",
        description="OOP practice",
    )

    complete_use_case.execute(task.id)

    with pytest.raises(ValueError):
        complete_use_case.execute(task.id)


# =========================
# GET TASK
# =========================


def test_should_get_task_by_id(create_use_case, get_use_case) -> None:
    task = create_use_case.execute(
        title="Learn Clean Architecture",
        description="Study use cases",
    )

    found_task = get_use_case.execute(task.id)

    assert found_task.id == task.id
    assert found_task.title == "Learn Clean Architecture"


def test_should_raise_error_when_task_not_found(get_use_case) -> None:
    import uuid

    with pytest.raises(ValueError):
        get_use_case.execute(uuid.uuid4())


# =========================
# DELETE TASK
# =========================


def test_should_delete_task_successfully(
    create_use_case,
    delete_use_case,
    get_use_case,
) -> None:
    task = create_use_case.execute(
        title="Task to delete",
        description="Delete me",
    )

    delete_use_case.execute(task.id)

    with pytest.raises(ValueError):
        get_use_case.execute(task.id)


def test_should_not_delete_completed_task(
    create_use_case,
    complete_use_case,
    delete_use_case,
) -> None:
    task = create_use_case.execute(
        title="Important task",
        description="Cannot delete this",
    )

    complete_use_case.execute(task.id)

    with pytest.raises(ValueError):
        delete_use_case.execute(task.id)


# =========================
# LIST TASKS
# =========================


def test_should_list_all_tasks(
    create_use_case,
    list_use_case,
) -> None:
    create_use_case.execute(
        title="Task 1",
        description="First task",
    )

    create_use_case.execute(
        title="Task 2",
        description="Second task",
    )

    tasks = list_use_case.execute()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_should_return_empty_list_when_no_tasks_exist(
    list_use_case,
) -> None:
    tasks = list_use_case.execute()

    assert tasks == []
