import unittest
import xmlrunner
from SlidePuzzle  import puzzle


class PuzzleTest(unittest.TestCase):

    def test_start(self):
        sp = puzzle.SlidePuzzle()
        self.assertEqual(str(sp).count("|"), 12 )


def all_tests():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(PuzzleTest),
    ])

if __name__ == '__main__':

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

