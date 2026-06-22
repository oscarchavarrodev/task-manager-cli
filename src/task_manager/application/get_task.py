from uuid import UUID

from task_manager.domain.task import Task
from task_manager.application.ports.task_repository import TaskRepository


class GetTaskUseCase:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self, task_id: UUID) -> Task:
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise ValueError(f"Task with id {task_id} not found")

        return task
