from urllib.parse import urlparse

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
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.close()

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()