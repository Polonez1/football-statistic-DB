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
    tunnel.close()


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


if "__main__" == __name__:
    pass
