import click
import main


@click.command(name="season_data")
def seasonal_data():
    main.seasonal_data_update()


@click.command(name="historical_data")
def historical_data():
    # main.update_teams()
    main.historical_data_load()


@click.command(name="current")
def current_data():
    # main.update_teams()
    main.current_data_update()


@click.command(name="update_teams")
def update_teams():
    main.update_teams()
    print("Ok")


@click.command()
def hello():
    print("Hello, World!")


@click.group()
def cli():
    pass


cli.add_command(hello)
cli.add_command(update_teams)

if __name__ == "__main__":
    cli()
