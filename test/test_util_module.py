__author__ = 'aj'

import unittest
import sys
from xml.dom import *


sys.path.append("../")
sys.path.append("../src/")
from utils.util import *


class TestUtil(unittest.TestCase):
    def test_get_data_from_xml_file_method_returns_a_list(self):
        result = get_data_from_xml_file('../src/db/entities/users.xml', 'User')
        self.assertIsInstance(result, type([]))

    def test_import_movies_from_xml_file_method(self):
        movie_list = import_movies_from_xml_file()
        print movie_list

if __name__ == "__main__":
    unittest.main()
