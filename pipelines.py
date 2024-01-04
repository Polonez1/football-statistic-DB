from API import data_collector as APIrequest
from SQL import ssh_sql_connector as SQL
from DataProcessing import data_transform as transform
from DataProcessing import reordered_col
from DataProcessing import additional_transform as add_data

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


if "__main__" == __name__:
    seasonal = SeasonalData()
    df = seasonal.update_countries_data()
