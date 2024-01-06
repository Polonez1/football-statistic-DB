import src.pysql.pySQL as sqlconn
import SQL.conn as conn
import pandas as pd
from datetime import datetime


ssh = sqlconn.SSHtunnel(
    ssh_host=conn.ssh_host,
    ssh_username=conn.ssh_username,
    ssh_password=conn.ssh_password,
    remote_bind_address=conn.remote_bind_address,
)
tunnel = ssh.create_tunnel()
tunnel.start()
sql = sqlconn.SQL(
    host=conn.host,
    database=conn.database,
    user=conn.user,
    password=conn.password,
    port=tunnel.local_bind_port,
    connect_type="MySQL",
)


def load_log_table(
    table_name: str, table_shape: pd.DataFrame.shape, success: bool, error: str = None
):
    name: str = "data_log"
    if success:
        result = "succes"
    else:
        result = "failed"
    df = pd.DataFrame(
        {
            "table_name": [table_name],
            "updated_at": [datetime.now()],
            "table_shape": [str(table_shape)],
            "result": [result],
            "error": [error],
        }
    )
    sql.load_data_to_SQL(df=df, table=name)


def data_loader(name: str, df: pd.DataFrame, truncate: bool = True):
    try:
        sql.load_data_to_SQL(
            df=df,
            table=name,
            truncate=truncate,
        )
        success = True
        error_message = None
    except Exception as e:
        success = False
        error_message = str(e)
        print(f"\033[91m {error_message} \033[0m")
    load_log_table(
        table_name=name, table_shape=df.shape, success=success, error=error_message
    )


def __delete_last_coma(element_list: list):
    if len(element_list) > 1:
        return str(tuple(element_list))
    string = str(tuple(element_list))
    last_comma_index = string.rfind(",")
    if last_comma_index != -1:
        modified_string = string[:last_comma_index] + string[last_comma_index + 1 :]
        return modified_string


def get_standings_data_from_sql():
    with open("./SQL/SQL_queries.sql/standings_data.sql", "r") as file:
        query = file.read()
    df = sql.get_data_from_query(query=query)
    standings_dict = df.to_dict(orient="records")
    return standings_dict


def get_leagues_id_list(tracked_football_countries, tracked_football_leagues):
    with open("./SQL/SQL_queries.sql/leagues_list.sql", "r") as file:
        query = file.read()
    params = {
        "countries": __delete_last_coma(tracked_football_countries),
        "leagues": __delete_last_coma(tracked_football_leagues),
    }
    df = sql.get_data_from_query(query=query, params=params)
    leagues_id_list = list(df["id"])

    return leagues_id_list


def get_fixtures_id_list(tracked_football_leagues, tracked_football_seasons):
    with open("./SQL/SQL_queries.sql/fixtures_list.sql", "r") as file:
        query = file.read()
    params = {
        "leagues": __delete_last_coma(tracked_football_leagues),
        "season": __delete_last_coma(tracked_football_seasons),
    }
    df = sql.get_data_from_query(query=query, params=params)
    fixture_id_list = list(df["fixture_id"])
    return fixture_id_list


def standings_data_delete(name: str, current_season: int):
    sql.read_query(query=f"""DELETE FROM {name} WHERE season = {current_season};""")

    return None


def data_delete_by_stats_id(name: str, stats_id: tuple):
    sql.read_query(query=f"""DELETE FROM {name} WHERE stats_id in {stats_id};""")

    return None


if "__main__" == __name__:
    pass
