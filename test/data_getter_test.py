import os
import unittest

import yaml

import data_getter


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_query_string_not_empty():
        assert data_getter.graph_query != ""

    @staticmethod
    def test_yaml_test_string():
        os.chdir(os.path.dirname(__file__))
        with open('../sql.yaml') as f:
            test_string = yaml.safe_load(f)["test"]
        assert test_string == "test"

    @staticmethod
    def test_get_data_not_none():
        data = data_getter.get_chart_data(False)
        assert len(data) > 0


if __name__ == '__main__':
    unittest.main()
