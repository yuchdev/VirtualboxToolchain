import os
import unittest
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

    def test_replace_string(self):
        """
        Test search and replace in string
        """
        old_text = "Lorem Ipsum"
        new_text = "Dolor Sit Amet"
        new_content = search_replace(OLD_CONTENT, old_text, new_text)
        self.assertEqual(NEW_CONTENT, new_content)

    def test_replace_file(self):
        """
        Test search and replace in file
        """
        lorem_ipsum_file = os.abs
        replace_infile()


if __name__ == "__main__":
    unittest.main()