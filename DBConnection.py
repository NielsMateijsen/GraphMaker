from urllib.parse import urlparse
import pandas.io.sql as sqlio

from dotenv import load_dotenv, find_dotenv
import os
import psycopg2


class DBConnection:
    uri = ""

    def __init__(self):
        load_dotenv(find_dotenv("cred.env"))
        self.uri = os.getenv("DB_URI")
        uri_args = urlparse(self.uri)
        username = uri_args.username
        password = uri_args.password
        database = uri_args.path[1:]
        hostname = uri_args.hostname
        port = uri_args.port
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
