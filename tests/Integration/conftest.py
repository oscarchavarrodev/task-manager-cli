import pytest

from task_manager.application.complete_task import CompleteTaskUseCase
from task_manager.application.create_task import CreateTaskUseCase
from task_manager.application.delete_task import DeleteTaskUseCase
from task_manager.application.get_task import GetTaskUseCase
from task_manager.infrastructure.persistence.sqlite_task_repository import (
    SqliteTaskRepository,
)


@pytest.fixture
def repository(tmp_path):
    db_path = tmp_path / "test.db"

    repository = SqliteTaskRepository(str(db_path))

    yield repository

    repository.close()


@pytest.fixture
def create_use_case(repository):
    return CreateTaskUseCase(repository)


@pytest.fixture
def complete_use_case(repository):
    return CompleteTaskUseCase(repository)


@pytest.fixture
def delete_use_case(repository):
    return DeleteTaskUseCase(repository)


@pytest.fixture
def get_use_case(repository):
    return GetTaskUseCase(repository)
