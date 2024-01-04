import sys

sys.path.append("./API/")


import json
from pandas import json_normalize
import pandas as pd


def open_json(file_name, path: str = "./output/") -> json:
    """func to open json data

    Args:
        file_name (_type_): file name
        path (str, optional): file directory. Defaults to "./output/".

    Returns:
        _type_: json file
    """
    with open(f"{path}{file_name}", "r", encoding="utf-8") as file:
        data = json.load(file)

        return data


def country_data_processing(json_obj: json = None) -> pd.DataFrame:
    """Country data

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: country data
    """
    # data = open_json("country.json")
    data = json_obj["response"]
    df = pd.DataFrame(data)

    return df


def seasons_data_processing(json_obj: json = None) -> pd.DataFrame:
    """Available seasons in db

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: seasons data. No relation data.
    """
    # data = open_json("seasons.json")
    data = json_obj["response"]
    df = pd.DataFrame(data)
    df = df.rename(columns={0: "available_seasons"}, inplace=False)
    return df


def __create_leagues_general_data(json_obj: json, index: int) -> pd.DataFrame:
    """Split leagues data to general data

    Args:
        json_obj (json): json from API
        index (int): index = id.

    Returns:
        pd.DataFrame: general data
    """
    league_df = pd.DataFrame(json_obj["league"], index=[index])
    country_df = pd.DataFrame(json_obj["country"], index=[index]).add_prefix("country_")
    df = pd.concat([league_df, country_df], axis=1)
    df["leagues_seasons_id"] = index
    return df


def __create_seasons_leagues_data(json_obj: json, index: int) -> pd.DataFrame:
    """Create a additional info about season from leagues data. This data have info about available data in season
    Args:
        json_obj (json): json from API
        index (int): index = id.

    Returns:
        pd.DataFrame: additional leagues data
    """
    seasons_data = json_obj["seasons"]
    seasons_data = json_normalize(data=seasons_data, sep="_")
    seasons_data["leagues_seasons_id"] = index
    df = pd.DataFrame(seasons_data).add_prefix("seasons_")
    return df


def leagues_data_processing(json_obj: json = None) -> pd.DataFrame:
    """Create leagues table and leagues info table. Realtion: leagues_season_id

    Args:
        json_obj (json, optional): json object from API. Defaults to None.

    Returns:
        pd.DataFrame: leagues table and leagues_season table
    """
    # data = open_json("leagues.json")
    data = json_obj["response"]
    index = 0

    full_data_leagues = []
    full_data_leagues_seasons = []
    for i in data:
        leagues_general_df = __create_leagues_general_data(json_obj=i, index=index)
        leagues_seasons_df = __create_seasons_leagues_data(json_obj=i, index=index)

        full_data_leagues.append(leagues_general_df)
        full_data_leagues_seasons.append(leagues_seasons_df)
        index += 1

    leagues = pd.concat(full_data_leagues)
    leagues_seasons = pd.concat(full_data_leagues_seasons)
    leagues_seasons = leagues_seasons.rename(
        columns={"seasons_leagues_seasons_id": "leagues_seasons_id"}
    )
    return leagues, leagues_seasons


def venue_data_processing(json_obj: json = None) -> pd.DataFrame:
    """Data about stadions

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: venue data
    """
    # json_obj = open_json("venue.json")
    data = json_obj["response"]
    df = pd.DataFrame(data)

    return df


def teams_data_processing(json_obj: json = None) -> pd.DataFrame:
    """Data about teams

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: teams data
    """
    # json_obj = open_json("teams.json")
    data = json_obj["response"]
    full_data = []
    index = 0
    for i in data:
        team_df = pd.DataFrame(i["team"], index=[index])
        venue_df = pd.DataFrame(i["venue"], index=[index]).add_prefix("venue_")
        venue_df = venue_df["venue_id"]
        dff = pd.concat([team_df, venue_df], axis=1)
        index += 1
        full_data.append(dff)
    df = pd.concat(full_data)
    return df


# =====================================================================================#
#


def __unique_id_generator(param, additional_id: int):
    season = param["season"]
    league_id = param["league"]
    team_id = param["team"]
    id = str(season) + str(league_id) + str(team_id) + str(additional_id)
    return id


def __create_id(param):
    stats_id = __unique_id_generator(param=param, additional_id=101)
    fixtures_id = __unique_id_generator(param=param, additional_id=202)
    goals_id = __unique_id_generator(param=param, additional_id=303)
    records_id = __unique_id_generator(param=param, additional_id=404)
    lineups_id = __unique_id_generator(param=param, additional_id=505)
    cards_id = __unique_id_generator(param=param, additional_id=606)
    return stats_id, fixtures_id, goals_id, records_id, lineups_id, cards_id


def __create_general_stats_table(data: json, **kwargs):
    league_data = pd.DataFrame(data["league"], index=[0]).add_prefix("league_")[
        ["league_id", "league_country", "league_season"]
    ]
    team_data = pd.DataFrame(data["team"], index=[0]).add_prefix("team_")[
        ["team_id", "team_name"]
    ]
    clean_sheets_data = pd.DataFrame(data["clean_sheet"], index=[0]).add_prefix(
        "clean_sheet_"
    )
    failed_to_score_data = pd.DataFrame(data["failed_to_score"], index=[0]).add_prefix(
        "failed_to_score_"
    )
    penalty_data = pd.DataFrame(
        json_normalize(data["penalty"], sep="_"), index=[0]
    ).add_prefix("penalty_")
    full_data = [
        league_data,
        team_data,
        clean_sheets_data,
        failed_to_score_data,
        penalty_data,
    ]
    form_data = data["form"]
    general_table = pd.concat(full_data, axis=1)
    general_table["form"] = form_data
    general_table["stats_id"] = kwargs["stats_id"]
    general_table["fixtures_stats_id"] = kwargs["fixtures_id"]
    general_table["goals_stats_id"] = kwargs["goals_id"]
    general_table["records_stats_id"] = kwargs["records_id"]
    general_table["lineups_stats_id"] = kwargs["lineups_id"]
    general_table["cards_stats_id"] = kwargs["cards_id"]

    return general_table


def __create_additional_table(
    name: str, additionall_id: str, data: json, stats_id: str, param: json
):
    df = pd.DataFrame(json_normalize(data[f"{name}"], sep="_")).add_prefix(f"{name}_")
    df["season"] = param["season"]
    df["league_id"] = param["league"]
    df["team_id"] = param["team"]
    df["stats_id"] = stats_id
    df[f"{name}_stats_id"] = additionall_id

    return df


def teams_data_stats_processing(json_obj: json = None) -> pd.DataFrame:
    """Data about teams stats

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: teams data
    """
    data = json_obj["response"]
    param = json_obj["parameters"]
    stats_id, fixtures_id, goals_id, records_id, lineups_id, cards_id = __create_id(
        param=param
    )

    general_df = __create_general_stats_table(
        data=data,
        stats_id=stats_id,
        fixtures_id=fixtures_id,
        goals_id=goals_id,
        records_id=records_id,
        lineups_id=lineups_id,
        cards_id=cards_id,
    )
    fixtures_data = __create_additional_table(
        name="fixtures",
        additionall_id=fixtures_id,
        data=data,
        stats_id=stats_id,
        param=param,
    )
    goals_data = __create_additional_table(
        name="goals", additionall_id=goals_id, data=data, stats_id=stats_id, param=param
    )
    records_data = __create_additional_table(
        name="biggest",
        additionall_id=records_id,
        data=data,
        stats_id=stats_id,
        param=param,
    )
    lineups_data = __create_additional_table(
        name="lineups",
        additionall_id=lineups_id,
        data=data,
        stats_id=stats_id,
        param=param,
    )
    cards_data = __create_additional_table(
        name="cards",
        additionall_id=cards_id,
        data=data,
        stats_id=stats_id,
        param=param,
    )
    return general_df, fixtures_data, goals_data, records_data, lineups_data, cards_data


# -----------------STANDINGS---------------------------------------#
def __create_standings_general_table(json_obj: json, index: int):
    rank = json_obj["rank"]
    points = json_obj["points"]
    goaldiff = json_obj["goalsDiff"]
    group = json_obj["group"]
    form = json_obj["form"]
    status = json_obj["status"]
    description = json_obj["description"]
    return pd.DataFrame(
        {
            "rank": rank,
            "points": points,
            "goalsDiff": goaldiff,
            "group": group,
            "form": form,
            "status": status,
            "description": description,
        },
        index=[index],
    )


def __unpack_standings_stats_data(
    json_obj: json, index: str, data_type: str
) -> pd.DataFrame:
    """unpack statistic data in standings json file (all, home and away goals for/against)

    Args:
        json_obj (json): json from API
        index (str): index
        data_type (str): all, home, away

    Returns:
        pd.DataFrame: stats data
    """
    data = json_obj[data_type]
    gen_data_df = (
        pd.DataFrame(data, index=[index])
        .add_prefix(f"{data_type}_")
        .drop(columns=f"{data_type}_goals")
    )
    data_goals = data["goals"]
    data_goals_df = pd.DataFrame(data_goals, index=[index]).add_prefix(
        f"{data_type}_goals_"
    )
    all_data_full = pd.concat([gen_data_df, data_goals_df], axis=1)

    return all_data_full


def __create_standings_stats_data(json_obj: json, index: int) -> pd.DataFrame:
    all_data = __unpack_standings_stats_data(
        json_obj=json_obj, index=index, data_type="all"
    )
    home_data = __unpack_standings_stats_data(
        json_obj=json_obj, index=index, data_type="home"
    )
    away_data = __unpack_standings_stats_data(
        json_obj=json_obj, index=index, data_type="away"
    )

    df = pd.concat([all_data, home_data, away_data], axis=1)
    return df


def __reorder_standings_columns(df: pd.DataFrame):
    col_to_reorder = [
        "id",
        "league_id",
        "season",
        "team_name",
        "team_id",
        "rank",
        "points",
        "goalsDiff",
        "group",
        "form",
        "status",
        "description",
        "team_logo",
        "all_played",
        "all_win",
        "all_draw",
        "all_lose",
        "all_goals_for",
        "all_goals_against",
        "home_played",
        "home_win",
        "home_draw",
        "home_lose",
        "home_goals_for",
        "home_goals_against",
        "away_played",
        "away_win",
        "away_draw",
        "away_lose",
        "away_goals_for",
        "away_goals_against",
        "stats_id",
    ]
    return df[col_to_reorder]


def standings_data_processing(json_obj: json = None) -> pd.DataFrame:
    """create standings data

    Args:
        json_obj (json, optional): json from API. Defaults to None.

    Returns:
        pd.DataFrame: standings data
    """
    # json_obj = open_json("standings.json")
    data = json_obj["response"][0]["league"]["standings"][0]
    league_id = json_obj["response"][0]["league"]["id"]
    season = json_obj["parameters"]["season"]

    index = 0

    full_data = []
    for i in data:
        general_data = __create_standings_general_table(json_obj=i, index=index)
        team_data = pd.DataFrame(i["team"], index=[index]).add_prefix("team_")
        stats_data = __create_standings_stats_data(json_obj=i, index=index)
        dff = pd.concat([general_data, team_data, stats_data], axis=1)
        dff["league_id"] = league_id
        dff["id"] = (
            dff["team_id"].astype("str") + dff["league_id"].astype("str") + str(season)
        )
        full_data.append(dff)
        index += 1

    df = pd.concat(full_data)
    df["season"] = season
    df["stats_id"] = (
        df["season"].astype("str")
        + df["league_id"].astype("str")
        + df["team_id"].astype("str")
        + "101"
    )
    df = __reorder_standings_columns(df)
    return df


# ------------------------------FIXTURES-------------------------------------#
def __select_fixtures_event_col(df: pd.DataFrame):
    col_to_select = [
        "fixture_id",
        "type",
        "detail",
        "comments",
        "time_elapsed",
        "time_extra",
        "team_id",
        "team_name",
        "team_logo",
        "player_id",
        "player_name",
        "assist_id",
        "assist_name",
    ]
    return df[col_to_select]


def fixtures_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("fixtures.json")
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")
    df = pd.DataFrame(data_n)
    return df


def fixtures_event_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("fixtures_event.json")
    data = json_obj["response"]
    fixture_id = json_obj["parameters"]["fixture"]
    data_n = json_normalize(data, sep="_")
    df = pd.DataFrame(data_n)
    df["fixture_id"] = fixture_id
    # df = __select_fixtures_event_col(df)
    return df


def fixtures_stats_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("fixtures_stats.json")
    data = json_obj["response"]
    fixture_id = json_obj["parameters"]["fixture"]
    index = 0

    full_data = []
    for i in data:
        df_team = pd.DataFrame(i["team"], index=["value"]).add_prefix("team_")
        df_stats = pd.DataFrame(i["statistics"]).set_index("type").T
        dff = pd.concat([df_team, df_stats], axis=1)
        dff.index = [index]
        dff["fixtures_stats_team_id"] = str(fixture_id) + dff["team_id"].astype(str)
        full_data.append(dff)
        index += 1

    df = pd.concat(full_data)
    df["fixture_id"] = fixture_id
    return df


def player_by_fixtures_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("player_fixture.json")
    data = json_obj["response"]
    fixture_id = json_obj["parameters"]["fixture"]
    data_list = []

    for i in data:
        team_data = i["team"]
        players_data = i["players"]
        index = 0
        for ii in players_data:
            player_df = (
                pd.DataFrame(ii["player"], index=[index])
                .reset_index()
                .add_prefix("player_")
            )
            team_data_df = (
                pd.DataFrame(team_data, index=[index]).reset_index().add_prefix("team_")
            )
            stats_df = pd.DataFrame(
                json_normalize(ii["statistics"], sep="_")
            ).reset_index()
            dff = pd.concat([team_data_df, player_df, stats_df], axis=1)
            data_list.append(dff)
            index += 1

    df = pd.concat(data_list).drop(columns=["team_index", "player_index"])
    df["fixture_id"] = fixture_id
    df.insert(0, "fixture_id", df.pop("fixture_id"))
    return df


# def player_by_league_id_data_processing():
#    pass


# def player_by_team_id_data_processing():
#    pass


def team_squad_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("squad.json")
    data = json_obj["response"][0]["players"]
    team_id = json_obj["parameters"]["team"]
    df = pd.DataFrame(data)
    df["team_id"] = team_id

    return df


def __create_teams_df(json_obj: json, index: int) -> pd.DataFrame:
    team_data = json_obj["team"]
    team_data_without_colors = team_data.copy()
    team_data_without_colors.pop("colors", None)
    team_df = pd.DataFrame(team_data_without_colors, index=[index]).add_prefix("team_")

    return team_df


def __create_gen_df(json_obj: json, index: int):
    team_df = __create_teams_df(json_obj=json_obj, index=index)
    coach_data = json_obj["coach"]
    coach_df = pd.DataFrame(coach_data, index=[index]).add_prefix("coach_")
    formation = json_obj["formation"]
    gen_df = pd.concat([team_df, coach_df], axis=1)
    gen_df["formation"] = formation

    return gen_df


def lineups_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("lineups.json")
    fixture_id = json_obj["parameters"]["fixture"]
    data = json_obj["response"]

    gen_lineups_data = []
    players_lineups_data = []

    index = 0
    for i in data:
        gen_df = __create_gen_df(json_obj=i, index=index)
        gen_lineups_data.append(gen_df)
        startXI = i["startXI"]

        for ii in startXI:
            player = ii["player"]
            player_df = pd.DataFrame(player, index=[index])
            player_df["fixture_id"] = fixture_id
            player_df["team_id"] = gen_df["team_id"][0]
            players_lineups_data.append(player_df)

    general_df = pd.concat(gen_lineups_data)
    general_df["fixture_id"] = fixture_id

    lineups_data = pd.concat(players_lineups_data)

    return general_df, lineups_data


def injuries_by_team_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("injuries_team.json")
    team_id = json_obj["parameters"]["team"]
    season = json_obj["parameters"]["season"]
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")

    df = pd.DataFrame(data_n)
    df["team_id"] = team_id
    df["season"] = season

    return df


def injuries_by_fixtures_data_processing(json_obj: json = None) -> pd.DataFrame:
    # json_obj = open_json("injuries_fixtures.json")
    fixture_id = json_obj["parameters"]["fixture"]
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")

    df = pd.DataFrame(data_n)
    df["fixture_id"] = fixture_id

    return df


##########--------------------------ODDS---------------------------########
def bets_type_data_processing(json_obj: json = None) -> pd.DataFrame:
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")
    df = pd.DataFrame(data_n)
    return df


def books_data_processing(json_obj: json = None) -> pd.DataFrame:
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")
    df = pd.DataFrame(data_n)
    return df


def odds_maping_data_processing(json_obj: json = None) -> pd.DataFrame:
    data = json_obj["response"]
    data_n = json_normalize(data, sep="_")
    df = pd.DataFrame(data_n)
    return df


if "__main__" == __name__:
    # data_collector.injuries_by_fixtures(fixture_id=874675)
    df = fixtures_stats_data_processing()
    # df.to_excel("test2.xlsx")
    # print(df)
