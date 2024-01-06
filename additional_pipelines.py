from API import data_collector as APIrequest
from DataProcessing import data_transform as transform

import pandas as pd
import time


def __venue_data_by_country(country: str):
    """Updated every season"""
    json_obj = APIrequest.get_venue_data(country=country)
    df = transform.venue_data_processing(json_obj=json_obj)
    return df


def venue_data(country_list: dict):
    name: str = "venue"
    data_list = []
    for i in country_list:
        dff = __venue_data_by_country(country=i)
        data_list.append(dff)

    df = pd.concat(data_list)
    return df


def __get_teams_data(country: str):
    json_obj = APIrequest.get_team_information_data(country=country)
    df = transform.teams_data_processing(json_obj=json_obj)
    return df


def teams_data(country_list: list):
    name: str = "teams"
    data_list = []
    for i in country_list:
        dff = __get_teams_data(country=i)
        data_list.append(dff)

    df = pd.concat(data_list)
    return df


def __get_standings_data(season: str, league_id: int):
    json_obj = APIrequest.get_standings_data(season=season, league_id=league_id)
    df = transform.standings_data_processing(json_obj=json_obj)
    return df


def standings_data(season_list: list, league_list: list) -> pd.DataFrame:
    """Current data updated after round

    Args:
        season_list (list): seasons list
        league_list (list): league_list by league id

    Returns:
        pd.Dataframe: standings data
    """
    name: str = "standings"
    full_data = []
    for season in season_list:
        for league_id in league_list:
            dff = __get_standings_data(season=season, league_id=league_id)
            full_data.append(dff)
    df = pd.concat(full_data)
    return df


def __get_teams_stats_data(season: str, league_id: int, team_id: int) -> dict:
    json_obj = APIrequest.get_team_statistic_data(
        season=season, league_id=league_id, team_id=team_id
    )
    (
        general_df,
        fixtures_data,
        goals_data,
        records_data,
        lineups_data,
        cards_data,
    ) = transform.teams_data_stats_processing(json_obj=json_obj)
    return {
        "stats_standings": general_df,
        "stats_standings_fixtures": fixtures_data,
        "stats_standings_goals": goals_data,
        "stats_standings_records": records_data,
        "stats_standings_lineups": lineups_data,
        "stats_standings_cards": cards_data,
    }


def teams_stats_data(standings_dict: dict):
    """Current data updated after round. Load teams stats data

    Args:
        season_list (list): season list by season
        leagues_list (list): leagues list by id
        teams_list (list): teams list by id
        truncate (bool, optional): Truncate table before load. Defaults to True.

    Returns:
        _type_: teams table storage data about teams stats
    """
    full_stats_standings = []
    full_stats_standings_fixtures = []
    full_stats_standings_goals = []
    full_stats_standings_records = []
    full_stats_standings_lineups = []
    full_stats_standings_cards = []
    request_counter = 1
    for i in standings_dict:
        season = i["season"]
        league_id = i["league_id"]
        team_id = i["team_id"]
        data_dict = __get_teams_stats_data(
            season=season, league_id=league_id, team_id=team_id
        )
        full_stats_standings.append(data_dict["stats_standings"])
        full_stats_standings_fixtures.append(data_dict["stats_standings_fixtures"])
        full_stats_standings_goals.append(data_dict["stats_standings_goals"])
        full_stats_standings_records.append(data_dict["stats_standings_records"])
        full_stats_standings_lineups.append(data_dict["stats_standings_lineups"])
        full_stats_standings_cards.append(data_dict["stats_standings_cards"])
        request_counter += 1
        if request_counter % 300 == 0:
            time.sleep(60)
            print("Limited request: sleep 60s")

    data_dict = {
        "stats_standings": pd.concat(full_stats_standings),
        "stats_standings_fixtures": pd.concat(full_stats_standings_fixtures),
        "stats_standings_goals": pd.concat(full_stats_standings_goals),
        "stats_standings_records": pd.concat(full_stats_standings_records),
        "stats_standings_lineups": pd.concat(full_stats_standings_lineups),
        "stats_standings_cards": pd.concat(full_stats_standings_cards),
    }
    return data_dict


def __get_fixtures_data(season: str, league_id: int):
    json_obj = APIrequest.get_fixtures_data(season=season, league_id=league_id)
    df = transform.fixtures_data_processing(json_obj=json_obj)
    return df


def fixtures_data(season_list: list, league_list: list) -> pd.DataFrame:
    """Current data updated every day

    Args:
        season_list (list): seasons list
        league_list (list): league_list by league id

    Returns:
        pd.DataFrame: fixtures data
    """
    name: str = "fixtures"
    full_data = []
    request_couter = 1
    for season in season_list:
        for league_id in league_list:
            print(request_couter, end="\r")
            dff = __get_fixtures_data(season=season, league_id=league_id)
            full_data.append(dff)
            request_couter += 1
            if request_couter % 300 == 0:
                time.sleep(60)
                print("Request limit 300: sleep 60s")
    df = pd.concat(full_data)
    return df


def __get_fixtures_event_data(fixture_id: int) -> pd.DataFrame:
    json_obj = APIrequest.get_event_data(fixture_id=fixture_id)
    df = transform.fixtures_event_data_processing(json_obj=json_obj)
    return df


def fixtures_event_data(fixtures_list: list) -> pd.DataFrame:
    """Current data updated after matches

    Args:
        fixtures_list (list): fixtures list by fixture_id

    Returns:
        pd.DataFrame: fixture event data
    """
    name: str = "fixtures_event"
    full_data = []
    counter = 1
    for fixture_id in fixtures_list:
        dff = __get_fixtures_event_data(fixture_id=fixture_id)
        print(counter, end="\r")
        full_data.append(dff)
        counter += 1
        if counter % 300 == 0:
            print(f"limited request {counter}: sleep 60s")
            time.sleep(60)

    df = pd.concat(full_data)

    return df


def __get_fixtures_stats_data(fixture_id: int) -> pd.DataFrame:
    json_obj = APIrequest.get_fixture_stat_data(fixture_id=fixture_id)
    df = transform.fixtures_stats_data_processing(json_obj=json_obj)
    return df


def fixtures_stats_data(fixtures_list: list) -> pd.DataFrame:
    """Current data updated after matches

    Args:
        fixtures_list (list): fixtures list by id

    Returns:
        pd.DataFrame: fixtures stats data
    """
    name: str = "fixtures_stats"
    full_data = []
    counter = 1
    c = 0
    for fixture_id in fixtures_list:
        dff = __get_fixtures_stats_data(fixture_id=fixture_id)
        print(counter, end="\r")
        full_data.append(dff)
        counter += 1
        c += 1
        if counter % 300 == 0:
            print(f"limited request {counter}: sleep 60s")
            time.sleep(60)
    df = pd.concat(full_data)
    return df


def __get_player_by_fixture_id(fixture_id: int):
    json_obj = APIrequest.player_by_fixture_id(fixture_id=fixture_id)
    df = transform.player_by_fixtures_data_processing(json_obj=json_obj)
    return df


def player_by_fixture_data(fixtures_list: list) -> pd.DataFrame:
    """Current data updated after match

    Args:
        fixtures_list (list): fixtures list by id

    Returns:
        pd.DataFrame: players statistic in match
    """
    name: str = "player_fixture"
    full_data = []
    counter = 1
    for fixture_id in fixtures_list:
        dff = __get_player_by_fixture_id(fixture_id=fixture_id)
        print(counter, end="\r")
        full_data.append(dff)
        counter += 1
        if counter % 300 == 0:
            print(f"limited request {counter}: sleep 60s")
            time.sleep(60)
    df = pd.concat(full_data)
    return df


def __get_team_squad(team_id: int):
    json_obj = APIrequest.get_team_squad(team_id=team_id)
    df = transform.team_squad_data_processing(json_obj=json_obj)
    return df


def team_squad_data(team_list: list):
    """Updated every season

    Args:
        team_list (list): team list by id

    Returns:
        _type_: team current season squad
    """
    name: str = "squad"
    full_data = []
    for team_id in team_list:
        dff = __get_team_squad(team_id=team_id)
        full_data.append(dff)
    df = pd.concat(full_data)
    return df


def __get_lineups(fixture_id: int) -> pd.DataFrame:
    json_obj = APIrequest.get_lineups(fixture_id=fixture_id)
    general_df, lineups_data = transform.lineups_data_processing(json_obj=json_obj)
    return general_df, lineups_data


def lineups_data(fixtures_list: list):
    name: str = "lineups"
    name_general: str = "lineups_info"
    name_additional: str = "lineups"

    general_data = []
    additional_data = []
    counter = 1
    for fixture_id in fixtures_list:
        general_df, additional_df = __get_lineups(fixture_id=fixture_id)
        print(counter, end="\r")
        general_data.append(general_df)
        additional_data.append(additional_df)
        counter += 1
        if counter % 300 == 0:
            print(f"limited request {counter}: sleep 60s")
            time.sleep(60)

    gen_df = pd.concat(general_data)
    addt_df = pd.concat(additional_data)
    return gen_df, addt_df


def __get_injuries_by_team(team_id: int, season: str) -> pd.DataFrame:
    json_obj = APIrequest.injuries_by_team(team_id=team_id, season=season)
    df = transform.injuries_by_team_data_processing(json_obj=json_obj)
    return df


def injuries_by_team_data(teams_list: list, season_list: list) -> pd.DataFrame:
    """Current data updated before every round

    Args:
        teams_list (list): teams list by id

    Returns:
        pd.DataFrame: injuries by team
    """
    name: str = "injuries_team"
    full_data = []
    for season in season_list:
        for team_id in teams_list:
            dff = __get_injuries_by_team(team_id=team_id, season=season_list)
            dff["season"] = season
            full_data.append(dff)
    df = pd.concat(full_data)
    return df


def __get_injuries_by_fixture(fixture_id: int) -> pd.DataFrame:
    json_obj = APIrequest.injuries_by_fixtures(fixture_id=fixture_id)
    df = transform.injuries_by_fixtures_data_processing(json_obj=json_obj)
    return df


def injuries_by_fixture_data(fixtures_list: list) -> pd.DataFrame:
    """Current data updated before every round

    Args:
        teams_list (list): teams list by id

    Returns:
        pd.DataFrame: injuries by fixtures
    """
    name: str = "injuries_fixtures"
    full_data = []
    counter = 1
    for fixture_id in fixtures_list:
        dff = __get_injuries_by_fixture(fixture_id=fixture_id)
        print(counter, end="\r")
        full_data.append(dff)
        counter += 1
        if counter % 300 == 0:
            print(f"limited request {counter}: sleep 60s")
            time.sleep(60)

    df = pd.concat(full_data)
    return df
