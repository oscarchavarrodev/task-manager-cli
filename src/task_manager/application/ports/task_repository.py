from typing import Protocol
from task_manager.domain.task import Task


class TaskRepository(Protocol):
    def save(self, task: Task) -> None:
        """Saves a task to the repository."""
        ...

    def get_by_id(self, task_id: str) -> Task:
        """Retrieves a task by its ID."""
        ...

    def delete(self, task_id: str) -> None:
        """Deletes a task by its ID."""
        ...

    def list_all(self) -> list[Task]:
        """Lists all tasks in the repository."""
        ...
