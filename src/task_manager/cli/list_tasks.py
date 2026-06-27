import typer

list_app = typer.Typer()


@list_app.callback(invoke_without_command=True)
def list_tasks():
    print("Listing tasks...")
