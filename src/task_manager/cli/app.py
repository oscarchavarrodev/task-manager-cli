import typer

from task_manager.cli.create import create_app
from task_manager.cli.complete import complete_app
from task_manager.cli.delete import delete_app
from task_manager.cli.get import get_app
from task_manager.cli.list_tasks import list_app

app = typer.Typer(help="Task Manager CLI")

app.add_typer(create_app, name="create")
app.add_typer(complete_app, name="complete")
app.add_typer(delete_app, name="delete")
app.add_typer(get_app, name="get")
app.add_typer(list_app, name="list")


if __name__ == "__main__":
    app()
