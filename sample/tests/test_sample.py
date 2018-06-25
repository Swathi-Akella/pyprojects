import unittest


class SampleTest(unittest.TestCase):
    def test_pass(self):
        return

    def test_fail(self):
        self.assertFalse(True)

    def test_error(self):
        raise RuntimeError('Testing Error')


class FailureMessageTest(unittest.TestCase):
    def test_fail_message(self):
        self.assertFalse(True, "Test failed")


class TruthTest(unittest.TestCase):
    def test_assert_True(self):
        self.assertTrue('a' == 'a')

    def test_assert_False(self):
        self.assertFalse('a' == 'b')

