import typer

complete_app = typer.Typer()


@complete_app.callback(invoke_without_command=True)
def complete():
    print("Completing task...")
