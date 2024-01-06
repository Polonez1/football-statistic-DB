from pipelines import SeasonalData, HistoricalData, CurrentData
import time


def seasonal_data_update():
    seasonal = SeasonalData()
    av_countries = seasonal.update_countries_data()
    av_season = seasonal.update_seasons_data()
    leagues = seasonal.update_leagues_data()
    venue = seasonal.update_venue_data()
    teams = seasonal.update_teams_data()


def historical_data_load():
    historical = HistoricalData()
    # standings = historical.load_standings_data()
    # team_statistic = historical.load_teams_statistic_data()
    # fixtures = historical.load_fixtures_data()
    # fixtures_event = historical.load_fixtures_event_data()

    # fixtures_stats = historical.load_fixtures_stats_data()
    # player_fixtures = historical.load_player_by_fixture_data()
    # lineups = historical.load_lineups_data()
    # injuries = historical.load_injuries_by_fixtures()


def current_data_update():
    current = CurrentData()
    # standings = current.update_current_standings_data()
    teams_statistic = current.update_current_teams_statistic_data()


if "__main__" == __name__:
    current_data_update()
