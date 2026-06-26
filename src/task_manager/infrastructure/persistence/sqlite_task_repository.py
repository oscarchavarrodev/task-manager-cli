import sqlite3
from datetime import datetime
from uuid import UUID

from task_manager.domain.enums import TaskStatus
from task_manager.domain.task import Task


class SqliteTaskRepository:
    def __init__(self, db_path: str = "tasks.db") -> None:
        self.connection = sqlite3.connect(db_path)

        self._create_table()

    def _create_table(self) -> None:
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """)

        self.connection.commit()

    def save(self, task: Task) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO tasks (
                id,
                title,
                description,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                str(task.id),
                task.title,
                task.description,
                task.status.name,
                task.created_at.isoformat(),
                task.updated_at.isoformat(),
            ),
        )

        self.connection.commit()

    def get_by_id(self, task_id: UUID) -> Task | None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                description,
                status,
                created_at,
                updated_at
            FROM tasks
            WHERE id = ?
            """,
            (str(task_id),),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Task(
            id=UUID(row[0]),
            title=row[1],
            description=row[2],
            status=TaskStatus[row[3]],
            created_at=datetime.fromisoformat(row[4]),
            updated_at=datetime.fromisoformat(row[5]),
        )

    def get_all(self) -> list[Task]:
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT
                id,
                title,
                description,
                status,
                created_at,
                updated_at
            FROM tasks
            """)

        rows = cursor.fetchall()

        return [
            Task(
                id=UUID(row[0]),
                title=row[1],
                description=row[2],
                status=TaskStatus[row[3]],
                created_at=datetime.fromisoformat(row[4]),
                updated_at=datetime.fromisoformat(row[5]),
            )
            for row in rows
        ]

    def delete(self, task_id: UUID) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ? 
            """,
            (str(task_id),),
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
