from API import data_collector as APIrequest
from SQL import ssh_sql_connector as SQL
from DataProcessing import data_transform as transform
from DataProcessing import reordered_col
from DataProcessing import additional_transform as add_data
import additional_pipelines

import config
import function_log as log

import pandas as pd


class SeasonalData:
    def __init__(self):
        self.season = None
        self.country_list = config.TRACKED_FOOTBALL_COUNTRIES

    @log.tables_load_info
    def update_countries_data(self):
        """Updated every season. Load av_countries table
        Args:
            truncate (bool, optional): Truncate table before load. Defaults to True.
        Returns:
            pd.DataFrame: available countries in database
        """
        name: str = "av_countries"
        json_obj = APIrequest.get_countries_data()
        df = transform.country_data_processing(json_obj=json_obj)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.av_countries_col]
        SQL.data_loader(name=name, df=df, truncate=True)
        return df

    @log.tables_load_info
    def update_seasons_data(self):
        """Updated every season. Load av_seasons table
        Args:
            truncate (bool, optional): Truncate table before load. Defaults to True.
        Returns:
            pd.DataFrame: available seasons in database
        """
        name: str = "av_season"
        json_obj = APIrequest.get_seasons_data()
        df = transform.seasons_data_processing(json_obj=json_obj)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.av_season_col]
        SQL.data_loader(name=name, df=df, truncate=True)

        return df

    @log.tables_load_info
    def update_leagues_data(self):
        """Updated ever season. Load leagues_info and leagues_additonal tables

        Args:
            truncate (bool, optional): Truncate table before load. Defaults to True.

        Returns:
            pd.DataFrame: general leagues table storage info about leagues and additional leagues table storage info about data's availables
        """
        name_fact_table: str = "leagues_info"
        name_additional_table: str = "leagues_additional"
        json_obj = APIrequest.get_leagues_data()
        general_leagues, additional_leagues = transform.leagues_data_processing(
            json_obj=json_obj
        )
        SQL.data_loader(
            name=name_fact_table,
            df=general_leagues[reordered_col.leagues_info_col],
            truncate=False,
        )
        SQL.data_loader(
            name=name_additional_table,
            df=additional_leagues[reordered_col.leagues_additional_col],
            truncate=False,
        )
        return general_leagues, additional_leagues

    @log.tables_load_info
    def update_venue_data(self):
        """Updated every season. Load venue data

        Args:
            country_list (dict): country list by name
            truncate (bool, optional): Truncate table before load. Defaults to True.

        Returns:
            _type_: data about stadion capacity, address and etc...
        """
        name: str = "venue"
        country_list = self.country_list
        df = additional_pipelines.venue_data(country_list=country_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.venue_col]
        SQL.data_loader(name=name, df=df, truncate=False)

        return df

    @log.tables_load_info
    def update_teams_data(self):
        """Updated every season. Load teams data

        Args:
            country_list (list): country list by name
            truncate (bool, optional): Truncate table before load. Defaults to True.

        Returns:
            _type_: teams table storage data about teams info
        """
        name: str = "teams"
        df = additional_pipelines.teams_data(country_list=self.country_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.teams_col]
        SQL.data_loader(name=name, df=df, truncate=False)
        return df


class HistoricalData:
    def __init__(self):
        self.season = config.TRACKED_HISTORICAL_SEASONS
        self.country_list = config.TRACKED_FOOTBALL_COUNTRIES
        # self.leagues_list = data.get_leagues_id_list()
        # self.fixtures_list = data.get_fixtures_id_list()

    @log.tables_load_info
    def load_standings_data(self):
        name: str = "standings"
        df = additional_pipelines.standings_data(country_list=self.country_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.standings_col]
        SQL.data_loader(name=name, df=df, truncate=False)

        return df

    @log.tables_load_info
    def load_teams_statistic_data(self):
        standings_dict = SQL.get_standings_data_from_sql()
        data_dict = additional_pipelines.teams_stats_data(standings_dict=standings_dict)
        stats_standings_col = reordered_col.stats_standings_col_dict
        for name in data_dict.keys():
            df = data_dict[name]
            SQL.data_loader(name=name, df=df[stats_standings_col[name]], truncate=False)
        return (
            data_dict["stats_standings"],
            data_dict["stats_standings_fixtures"],
            data_dict["stats_standings_goals"],
            data_dict["stats_standings_records"],
            data_dict["stats_standings_lineups"],
            data_dict["stats_standings_cards"],
        )

    @log.tables_load_info
    def load_fixtures_data(self):
        name: str = "fixtures"
        league_list = SQL.get_leagues_id_list(
            tracked_football_countries=config.TRACKED_FOOTBALL_COUNTRIES,
            tracked_football_leagues=config.TRACKED_FOOTBALL_LEAGUES,
        )

        df = additional_pipelines.fixtures_data(
            season_list=self.season, league_list=league_list
        )
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.fixtures_col]
        SQL.data_loader(name=name, df=df, truncate=False)
        return df

    @log.tables_load_info
    def load_fixtures_event_data(self):
        name: str = "fixtures_event"
        fixtures_list = SQL.get_fixtures_id_list()
        df = additional_pipelines.fixtures_event_data(fixtures_list=fixtures_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.fixtures_event_col]
        SQL.data_loader(name=name, df=df, truncate=False)

        return df

    @log.tables_load_info
    def load_fixtures_stats_data(self):
        name: str = "fixtures_stats"
        fixtures_list = SQL.get_fixtures_id_list()
        df = additional_pipelines.fixtures_stats_data(fixtures_list=fixtures_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.fixtures_stats_col]
        SQL.data_loader(name=name, df=df, truncate=False)
        return df

    @log.tables_load_info
    def load_player_by_fixture_data(self):
        name: str = "player_fixture"
        fixtures_list = SQL.get_fixtures_id_list()
        df = additional_pipelines.player_by_fixture_data(fixtures_list=fixtures_list)
        df = add_data.add_updated_at_col(df=df)
        df = df[reordered_col.player_fixture_col]
        SQL.data_loader(name=name, df=df, truncate=False)

        return df

    @log.tables_load_info
    def load_lineups_data(self):
        name_general: str = "lineups_info"
        name_additional: str = "lineups"
        fixtures_list = SQL.get_fixtures_id_list()
        lineups, lineups_info = additional_pipelines.lineups_data(
            fixtures_list=fixtures_list
        )
        lineups = lineups[reordered_col.lineups_info_col]
        lineups = add_data.add_updated_at_col(df=lineups)

        lineups_info = lineups_info[reordered_col.lineups_col]
        lineups_info = add_data.add_updated_at_col(df=lineups_info)

        SQL.data_loader(name=name_general, df=lineups, truncate=False)
        SQL.data_loader(name=name_additional, df=lineups_info, truncate=False)

        return lineups, lineups_info

    def load_injuries_by_fixtures(self):
        name: str = "injuries_fixtures"
        fixtures_list = SQL.get_fixtures_id_list()
        df = additional_pipelines.injuries_by_fixture_data(fixtures_list=fixtures_list)
        df = df[reordered_col.injuries_fixtures_col]
        SQL.data_loader(name=name, df=df, truncate=False)

        return df


if "__main__" == __name__:
    seasonal = SeasonalData()
    df = seasonal.update_seasons_data()
