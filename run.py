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


if __name__ == "__main__":
    historical_data()
