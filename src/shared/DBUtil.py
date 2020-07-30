from sqlalchemy import create_engine
from .CommonUtil import CommonUtil


class DBUtil():
    DATA_BASE = 'Heroku'
    dielect = None

    def __init__(self):
        self.dielect = 'postgresql'

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_db_connection(self):
        com_obj = CommonUtil()
        eng_obj = None
        try:
            conn_str = com_obj.get_db_constring()
            #print(conn_str)
            engine = create_engine(conn_str)
            eng_obj = engine
            return eng_obj
        except:
            raise
        finally:
            return eng_obj

    def execute_custom_select(self, query):
        connection = self.get_db_connection()
        results = connection.execute(query).fetchall()
        return results

    def execute_custom_query(self, query):
        connection = self.get_db_connection()
        results = connection.execute(query).fetchall()
        return results

    def execute_custom_function(self, function_name):
        connection = self.get_db_connection()
        connection.row_factory = self.dict_factory
        results = connection.execute(function_name).fetchall()
        #results = connection
        return results

