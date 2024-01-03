import src.pysql.pySQL as sqlconn
import conn


class DataLoad(sqlconn.SQL):
    def __init__(self, connect_type, **kwargs):
        super().__init__(connect_type, **kwargs)

    def create_ssh_sql_conncector(self):
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
        return sql

    def select_data_from_DB(self, query: str):
        df = self.get_data_from_query(query=query)
        return df


if "__main__" == __name__:
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
