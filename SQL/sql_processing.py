import src.pysql.pySQL as sqlconn


class DataLoad(sqlconn.SQL):
    def __init__(self, connect_type, **kwargs):
        super().__init__(connect_type, **kwargs)

    def select_data_from_DB(self, query: str):
        df = self.get_data_from_query(query=query)
        return df


if "__main__" == __name__:
    sql = DataLoad(
        host="localhost",
        database="footstats",
        # user="user",
        # password="pass",
        connect_type="MsSQL",
    )
