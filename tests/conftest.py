import pytest

from task_manager.infrastructure.persistence.in_memory_task_repository import (
    InMemoryTaskRepository,
)
from task_manager.application.create_task import CreateTaskUseCase
from task_manager.application.complete_task import CompleteTaskUseCase
from task_manager.application.delete_task import DeleteTaskUseCase
from task_manager.application.get_task import GetTaskUseCase


@pytest.fixture
def repository():
    return InMemoryTaskRepository()


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
