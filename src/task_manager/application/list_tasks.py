from task_manager.application.ports.task_repository import TaskRepository
from task_manager.domain.task import Task


class ListTasksUseCase:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self) -> list[Task]:
        return self.repository.get_all()
