import unittest


class FixtureTest(unittest.TestCase):
    def setUp(self):
        print("invoked setUp()")
        self.test_list = [1, 2, 3]

    def tearDown(self):
        print("invoked tearDown()")
        del self.test_list

    def test_count(self):
        self.assertCountEqual([1, 2, 3], self.test_list)
