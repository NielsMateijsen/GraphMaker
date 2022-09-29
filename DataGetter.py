import os
import pandas.io.sql as sqlio

from DBConnection import DBConnection
import yaml


class DataGetter:
    graph_query = ""

    os.chdir(os.path.dirname(__file__))
    with open('sql.yaml') as f:
        try:
            graph_query = yaml.safe_load(f)["sql"]["graph"]
        except yaml.YAMLError as e:
            print(e)

    def get_data(self, is_guest):
        conn = DBConnection()
        if self.graph_query != "":
            data = conn.query(self.graph_query.format(str(is_guest)))
            conn.close()
            return data
        conn.close()
        raise Exception("\nEXCEPTION:\ngraph_query is empty")
