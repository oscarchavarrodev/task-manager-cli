from task_manager.domain.task import Task
from task_manager.infrastructure.persistence.sqlite_task_repository import (
    SqliteTaskRepository,
)


def test_should_save_and_retrieve_task() -> None:
    repository = SqliteTaskRepository("test_tasks.db")

    task = Task.create(
        title="Learn SQLite",
        description="Persistence layer",
    )

    repository.save(task)

    retrieved = repository.get_by_id(task.id)

    assert retrieved is not None
    assert retrieved.id == task.id
    assert retrieved.title == task.title
    assert retrieved.description == task.description
    assert retrieved.status == task.status

    repository.close()


def test_should_get_all_tasks() -> None:
    repository = SqliteTaskRepository("test_tasks.db")

    task1 = Task.create(
        title="Task 1",
        description="Description 1",
    )

    task2 = Task.create(
        title="Task 2",
        description="Description 2",
    )

    repository.save(task1)
    repository.save(task2)

    tasks = repository.get_all()

    task_ids = [task.id for task in tasks]

    assert task1.id in task_ids
    assert task2.id in task_ids

    repository.close()


def test_should_delete_task() -> None:
    repository = SqliteTaskRepository("test_tasks.db")

    task = Task.create(
        title="Task to delete",
        description="This task will be deleted",
    )

    repository.save(task)
    repository.delete(task.id)

    deleted_task = repository.get_by_id(task.id)

    assert deleted_task is None

    repository.close()
