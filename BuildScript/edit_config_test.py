import os
import shutil
import stat
import unittest
from log_helper import logger
from edit_config import search_replace, replace_infile


OLD_CONTENT = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""


NEW_CONTENT = """Dolor Sit Amet is simply dummy text of the printing and typesetting industry.
Dolor Sit Amet has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Dolor Sit Amet passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Dolor Sit Amet."""


class TestSearchReplace(unittest.TestCase):

    OLD_TEXT = "Lorem Ipsum"
    NEW_TEXT = "Dolor Sit Amet"

    def test_replace_string(self):
        """
        Test search and replace in string
        """
        new_content, num_occurrences = search_replace(OLD_CONTENT,
                                                      TestSearchReplace.OLD_TEXT,
                                                      TestSearchReplace.NEW_TEXT)
        self.assertEqual(NEW_CONTENT, new_content)

    def test_replace_file(self):
        """
        Test search and replace in file
        """
        lorem_ipsum = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lorem_ipsum.txt")
        lorem_ipsum_copy = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lorem_ipsum.copy.txt")
        dolor_sit = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dolor_sit.txt")
        shutil.copyfile(lorem_ipsum, lorem_ipsum_copy)
        self.assertTrue(os.path.isfile(lorem_ipsum))
        self.assertTrue(os.path.isfile(lorem_ipsum_copy))
        self.assertTrue(os.path.isfile(dolor_sit))
        replace_infile(lorem_ipsum_copy, TestSearchReplace.OLD_TEXT, TestSearchReplace.NEW_TEXT)

        with open(lorem_ipsum_copy, 'r') as lorem_ipsum_file:
            lorem_ipsum_content = lorem_ipsum_file.read()

        with open(dolor_sit, 'r') as dolor_sit_file:
            dolor_sit_content = dolor_sit_file.read()

        self.assertEqual(lorem_ipsum_content, dolor_sit_content)
        os.unlink(lorem_ipsum_copy)


if __name__ == "__main__":
    unittest.main()
