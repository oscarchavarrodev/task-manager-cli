from task_manager.domain.task import Task
from task_manager.application.ports.task_repository import TaskRepository


class CreateTaskUseCase:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def execute(self, title: str, description: str) -> Task:
        task = Task.create(title=title, description=description)

        self.repository.save(task)

        return task
