import unittest


class PuzzleTest(unittest.TestCase):

    def test_start(self):
        self.assertFalse("Failure test.")


def all_tests():
    return unittest.TestSuite([
        PuzzleTest(),
    ])