from datetime import datetime
from uuid import uuid4

import pytest

from task_manager.domain.enums import TaskStatus
from task_manager.domain.task import Task


def test_should_raise_error_when_tittle_is_empty() -> None:
    with pytest.raises(ValueError):
        Task(
            id=uuid4(),
            title="",
            description="Test description",
            status=TaskStatus.PENDING,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )


def test_should_create_task_with_pending_status() -> None:
    task = Task.create(
        title="Learn DDD",
        description="Practice domain modeling",
    )

    assert task.status == TaskStatus.PENDING


def test_should_create_task_with_completed_status() -> None:
    task = Task.create(
        title="Learn DDD",
        description="Practice domain modeling",
    )
    task.complete()
    assert task.status == TaskStatus.COMPLETED


def test_should_not_complete_task_twice() -> None:
    task = Task.create(
        title="Learn Python",
        description="Practice OOP",
    )

    task.complete()

    with pytest.raises(ValueError):
        task.complete()
