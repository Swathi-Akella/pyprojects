import unittest
import textwrap


class TestContainer(unittest.TestCase):
    def test_count(self):
        self.assertCountEqual([1, 2, 3], [3, 2, 1],)
    
    def test_dict(self):
        self.assertDictEqual({'a':1,'b':2},{'a':3,'b':1})
        
    def test_list(self):
        self.assertListEqual([1,2,3],[1,2,3])
    
    def test_multiline_string(self):
        self.assertMultiLineEqual(
            textwrap.dedent("""
            This string
            has more than one
            line.
            """),
            textwrap.dedent("""
            This string
            has more than one
            line.
            """),
        )
