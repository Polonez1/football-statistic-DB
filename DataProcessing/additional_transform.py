import pandas as pd
from datetime import datetime


def add_updated_at_col(df: pd.DataFrame):
    df["source"] = "footballAPI"
    df["created_by"] = "https://github.com/Polonez1/football-statistic-DB"
    df["updated_at"] = datetime.now()
    return df
