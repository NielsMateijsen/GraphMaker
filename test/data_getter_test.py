import os
import unittest

import yaml

from DataGetter import DataGetter


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_query_string_not_empty():
        assert DataGetter.graph_query != ""

    @staticmethod
    def test_yaml_test_string():
        os.chdir(os.path.dirname(__file__))
        with open('../sql.yaml') as f:
            test_string = yaml.safe_load(f)["test"]
        assert test_string == "test"

    @staticmethod
    def test_get_data_not_none():
        getter = DataGetter()
        data = getter.get_chart_data(False)
        assert len(data) > 0


if __name__ == '__main__':
    unittest.main()
