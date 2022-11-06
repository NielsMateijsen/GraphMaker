import pandas.io.sql as sqlio

from dotenv import load_dotenv, find_dotenv
import os
import psycopg2


class DBConnection:

    def __init__(self):
        load_dotenv(find_dotenv("cred.env"))

        username = os.getenv("LOCAL_USERNAME")
        password = os.getenv("local_password")
        database = os.getenv("local_database")
        hostname = "localhost"
        port = os.getenv("local_port")

        self.conn = psycopg2.connect(
            database=database,
            user=username,
            password=password,
            host=hostname,
            port=port
        )

    def query(self, query):
        return sqlio.read_sql(query, self.conn)

    def close(self):
        self.conn.close()
