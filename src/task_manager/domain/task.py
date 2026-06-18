from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from task_manager.domain.enums import TaskStatus


@dataclass
class Task:
    id: UUID
    title: str
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if len(self.title) > 255:
            raise ValueError("Task title exceeds maximum length")

    @classmethod
    def create(
        cls,
        title: str,
        description: str,
    ) -> "Task":
        now = datetime.now()

        return cls(
            id=uuid4(),
            title=title,
            description=description,
            status=TaskStatus.PENDING,
            created_at=now,
            updated_at=now,
        )

    def complete(self) -> None:
        if self.status == TaskStatus.COMPLETED:
            raise ValueError("Task is already completed")

        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()
