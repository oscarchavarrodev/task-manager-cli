from uuid import UUID

from task_manager.domain.enums import TaskStatus
from task_manager.application.ports.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self, task_id: UUID) -> None:
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise ValueError("Task not found")

        if task.status == TaskStatus.COMPLETED:
            raise ValueError("Cannot delete completed task")

        self.repository.delete(task_id)
