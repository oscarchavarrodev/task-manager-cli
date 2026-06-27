import typer

from task_manager.application.create_task import CreateTaskUseCase
from task_manager.infrastructure.persistence.sqlite_task_repository import (
    SqliteTaskRepository,
)

create_app = typer.Typer()


@create_app.callback(invoke_without_command=True)
def create(
    title: str = typer.Option(..., help="Task title"),
    description: str = typer.Option(..., help="Task description"),
) -> None:
    repository = SqliteTaskRepository()

    use_case = CreateTaskUseCase(repository)

    task = use_case.execute(
        title=title,
        description=description,
    )

    repository.close()

    typer.secho(
        f"Task created successfully!\nID: {task.id}",
        fg=typer.colors.GREEN,
    )
