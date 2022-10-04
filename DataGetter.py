import os

import pandas as pd
from DBConnection import DBConnection
import yaml
from datetime import datetime


class DataGetter:
    graph_query = ""
    number_to_month = {
        1: "januari",
        2: "februari",
        3: "maart",
        4: "april",
        5: "mei",
        6: "juni",
        7: "juli",
        8: "augustus",
        9: "september",
        10: "oktober",
        11: "november",
        12: "december"
    }

    os.chdir(os.path.dirname(__file__))
    with open('sql.yaml') as f:
        try:
            graph_query = yaml.safe_load(f)["sql"]["graph"]
        except yaml.YAMLError as e:
            print(e)

    def get_chart_data(self, is_guest):
        conn = DBConnection()

        if self.graph_query == "":
            raise Exception("EXCEPTION: EMPTY DATA QUERY")

        df = conn.query(self.graph_query.format(str(is_guest)))
        conn.close()

        sort_order = self.get_sort_order()
        df["month"] = df["month"].apply(int)
        df["month"] = df["month"].map(self.number_to_month)
        df = df.pivot(values="count", index="month", columns="naam")

        df.index = pd.Categorical(df.index, sort_order)
        df = df.sort_index()

        df.fillna(0, inplace=True)

        return df

    def get_sort_order(self):
        current_month = datetime.now().month

        a = list(range(1, 13))

        def map_function(x):
            if x + current_month < 13:
                month_int = x + current_month
            else:
                month_int = (x + current_month + 1) % 13

            return self.number_to_month[month_int]

        return list(map(map_function, a))
