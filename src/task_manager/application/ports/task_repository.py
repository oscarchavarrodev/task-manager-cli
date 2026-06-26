from typing import Protocol
from uuid import UUID

from task_manager.domain.task import Task


class TaskRepository(Protocol):
    def save(self, task: Task) -> None: ...

    def get_by_id(self, task_id: UUID) -> Task | None: ...

    def delete(self, task_id: UUID) -> None: ...

    def get_all(self) -> list[Task]: ...
