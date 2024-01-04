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
