import os
import unittest

from dotenv import load_dotenv, dotenv_values, find_dotenv

from DBConnection import DBConnection


class MyTestCase(unittest.TestCase):
    db_connection = None

    def tearDown(self):
        if self.db_connection:
            self.db_connection.close()

    def test_db_connection(self):
        self.db_connection = DBConnection()
        assert self.db_connection is not None
        assert self.db_connection.conn.closed == 0

    def test_query(self):
        self.db_connection = DBConnection()
        result = self.db_connection.query("SELECT 1;")
        assert self.db_connection.conn.closed == 0
        assert result.iloc[0][0] == 1

    @staticmethod
    def test_env_getter():
        load_dotenv(find_dotenv("cred.env"))
        res = os.getenv("TEST_STRING")
        assert res == "test"


if __name__ == '__main__':
    unittest.main()
