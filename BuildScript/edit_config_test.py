import unittest
from edit_config import search_replace, replace_infile


class TestSearchReplace(unittest.TestCase):

    def test_replace_string(self):
        """
        Test search and replace in string
        """
        search_replace()

    def test_replace_file(self):
        """
        Test search and replace in file
        """
        replace_infile()


if __name__ == "__main__":
    unittest.main()