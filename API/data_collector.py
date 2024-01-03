from API.apifootball import make_api
import API.endpoints as endpoint
import json


def get_countries_data():
    url = endpoint.COUNTRIES_DATA
    json_obj = make_api(url=url)
    # with open("./output/country.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_seasons_data():
    url = endpoint.SEASONS_DATA
    json_obj = make_api(url=url)
    # with open("./output/seasons.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_leagues_data():
    url = endpoint.LEAGUES_DATA
    json_obj = make_api(url=url)
    # with open("./output/leagues.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_venue_data(country: str):
    url = endpoint.VENUE_DATA
    params = {"country": country}
    json_obj = make_api(url=url, params=params)
    # with open("./output/venue.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_team_information_data(country: str):
    url = endpoint.TEAM_INFORMATION
    params = {"country": f"{country}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/teams.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_team_statistic_data(season: str, league_id: int, team_id: int):
    url = endpoint.TEAM_STATISTIC
    params = {"league": f"{league_id}", "season": f"{season}", "team": f"{team_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/teams_stats.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)
    return json_obj


def get_standings_data(season: str, league_id: int):
    url = endpoint.STANDINGS_DATA
    params = {"season": season, "league": f"{league_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/standings.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_fixtures_data(season: str, league_id: int):
    url = endpoint.FIXTURES_DATA
    params = {"season": season, "league": f"{league_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/fixtures.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_event_data(fixture_id: int):
    url = endpoint.FIXTURES_EVENT
    params = {"fixture": f"{fixture_id}"}

    json_obj = make_api(url=url, params=params)
    # with open("./output/fixtures_event.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_fixture_stat_data(fixture_id: int):
    url = endpoint.FIXTURES_STATS
    params = {"fixture": f"{fixture_id}"}

    json_obj = make_api(url=url, params=params)
    # with open("./output/fixtures_stats.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def player_by_player_id(player_id: int, season: str):
    url = endpoint.PLAYER_BY_ID
    params = {"id": f"{player_id}", "season": season}

    json_obj = make_api(url=url, params=params)
    with open("./output/player.json", "w", encoding="utf-8") as json_file:
        json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    print(json_obj)


def player_by_fixture_id(fixture_id: int):
    url = endpoint.PLAYERS_BY_FIXTURE
    params = {"fixture": f"{fixture_id}"}

    json_obj = make_api(url=url, params=params)
    # with open("./output/player_fixture.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def player_by_league_id(league_id: int, seasons: str):
    url = endpoint.PLAYERS_BY_LEAGUE
    params = {"league": f"{league_id}", "season": seasons}

    json_obj = make_api(url=url, params=params)
    # with open("./output/player_league.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)
    #
    return json_obj


def player_by_team_id(team_id: int, seasons: str):
    url = endpoint.PLAYERS_BY_TEAM
    params = {"team": f"{team_id}", "season": seasons}

    json_obj = make_api(url=url, params=params)
    # with open("./output/player_team.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_team_squad(team_id: int):
    url = endpoint.PLAYER_SQUAD
    params = {"team": f"{team_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/squad.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_lineups(fixture_id: int):
    url = endpoint.LINEUPS
    params = {"fixture": f"{fixture_id}"}

    json_obj = make_api(url=url, params=params)
    # with open("./output/lineups.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_sidelined():
    pass


def injuries_by_team(team_id: int, season: str):
    url = endpoint.INJURIES_BY_TEAM
    params = {"season": season, "team": f"{team_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/injuries_team.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def injuries_by_fixtures(fixture_id: str):
    url = endpoint.INJURIES_BY_FIXTURES
    params = {"fixture": f"{fixture_id}"}
    json_obj = make_api(url=url, params=params)
    # with open("./output/injuries_fixtures.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


if "__main__" == __name__:
    l = get_countries_data()
    print(l)
