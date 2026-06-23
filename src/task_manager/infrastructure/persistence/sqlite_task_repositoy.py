import sqlite3


class SqliteTaskRepository:
    def __init__(self, db_path: str = "tasks.db") -> None:
        self.connection = sqlite3.connect(db_path)

        self._create_table()

    def _create_table(self) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL
            )
            """
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()