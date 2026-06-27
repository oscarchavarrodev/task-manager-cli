import typer

get_app = typer.Typer()


@get_app.callback(invoke_without_command=True)
def get():
    print("Getting task...")
