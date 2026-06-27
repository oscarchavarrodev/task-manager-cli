import typer

delete_app = typer.Typer()


@delete_app.callback(invoke_without_command=True)
def delete():
    print("Deleting task...")
