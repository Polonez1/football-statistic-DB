from API.apifootball import make_api
import API.endpoints as endpoint
import json


def get_bets_data():
    url = endpoint.BETS_DATA
    json_obj = make_api(url=url)
    # with open("./output/bets.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_books_data():
    url = endpoint.BOOKMAKERS_DATA
    json_obj = make_api(url=url)
    # with open("./output/bookmakers.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_odds_maping():
    url = endpoint.ODDS_MAPING
    json_obj = make_api(url=url)
    # with open("./output/odds_maping.json", "w", encoding="utf-8") as json_file:
    #    json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    return json_obj


def get_odds_by_league(league_id: int, season: str):
    url = endpoint.ODDS_BY_LEAGUE
    params = {"league": f"{league_id}", "season": season}
    json_obj = make_api(url=url, params=params)
    with open("./output/odds_maping.json", "w", encoding="utf-8") as json_file:
        json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    print(json_obj)


def get_odds_by_fixture(fixture_id: int):
    url = endpoint.ODDS_BY_FIXTURE
    params = {"fixture": f"{fixture_id}"}
    json_obj = make_api(url=url, params=params)
    with open("./output/odds_maping.json", "w", encoding="utf-8") as json_file:
        json.dump(json_obj, json_file, ensure_ascii=False, indent=2)

    print(json_obj)


if "__main__" == __name__:
    get_bets_data()
