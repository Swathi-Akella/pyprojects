import unittest


class EqualityTest(unittest.TestCase):
    def testExpectEqual(self):
        self.assertEqual(1, 4-3)

    def testExpectEqualFails(self):
        self.assertEqual(1, 3)

    def testExpectNotEqual(self):
        self.assertNotEqual(1, 2)

    def testExpectNotEqualFails(self):
        self.assertNotEquals(1, 1)
