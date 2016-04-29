import unittest
import xmlrunner
from SlidePuzzle  import puzzle


class PuzzleTest(unittest.TestCase):

    def test_12_bars(self):
        sp = puzzle.SlidePuzzle()
        self.assertEqual(str(sp).count("|"), 12)

    def test_initial_board(self):
        sp = puzzle.SlidePuzzle()
        initial_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 |   |"
        self.assertEqual(str(sp), initial_board)

    def test_can_move(self):
        sp = puzzle.SlidePuzzle()
        self.assertEqual(sp.can_move(1), False)
        self.assertEqual(sp.can_move(2), False)
        self.assertEqual(sp.can_move(3), False)
        self.assertEqual(sp.can_move(4), False)
        self.assertEqual(sp.can_move(5), False)
        self.assertEqual(sp.can_move(6), True)
        self.assertEqual(sp.can_move(7), False)
        self.assertEqual(sp.can_move(8), True)


def all_tests():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(PuzzleTest),
    ])

if __name__ == '__main__':

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

