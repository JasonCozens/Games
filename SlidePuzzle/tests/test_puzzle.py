import unittest
import xmlrunner
from SlidePuzzle import puzzle
from SlidePuzzle.puzzle import Direction


class MockRandom:

    def __init__(self, choices=[]):
        self._choices = choices
        self._choices.reverse()

    def choice(self, sequence):
        return self._choices.pop()


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

    def test_locked_tile_can_not_move(self):
        sp = puzzle.SlidePuzzle()
        sp.move(1)
        initial_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 |   |"
        self.assertEqual(str(sp), initial_board)

    def test_move_right(self):
        sp = puzzle.SlidePuzzle()
        sp.move(8)
        new_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 |   | 8 |"
        self.assertEqual(str(sp), new_board)

    def test_move_down(self):
        sp = puzzle.SlidePuzzle()
        sp.move(6)
        new_board = "| 1 | 2 | 3 |\n| 4 | 5 |   |\n| 7 | 8 | 6 |"
        self.assertEqual(str(sp), new_board)

    def test_move_right_move_left(self):
        sp = puzzle.SlidePuzzle()
        sp.move(8)
        sp.move(8)
        initial_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 |   |"
        self.assertEqual(str(sp), initial_board)

    def test_move_down_move_up(self):
        sp = puzzle.SlidePuzzle()
        sp.move(6)
        sp.move(6)
        initial_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 |   |"
        self.assertEqual(str(sp), initial_board)

    def test_move_space_up(self):
        sp = puzzle.SlidePuzzle()
        sp.move_space(Direction.Up)
        new_board = "| 1 | 2 | 3 |\n| 4 | 5 |   |\n| 7 | 8 | 6 |"
        self.assertEqual(str(sp), new_board)

    def test_move_space_left(self):
        sp = puzzle.SlidePuzzle()
        sp.move_space(Direction.Left)
        new_board = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 |   | 8 |"
        self.assertEqual(str(sp), new_board)

    def test_shuffle_zero_iterations(self):
        sp = puzzle.SlidePuzzle()
        board = str(sp)
        sp.shuffle(0)
        self.assertEqual(str(sp), board)

    def test_shuffle_up(self):
        sp = puzzle.SlidePuzzle(MockRandom([Direction.Up]))
        sp.shuffle(1)
        new_board = "| 1 | 2 | 3 |\n| 4 | 5 |   |\n| 7 | 8 | 6 |"
        self.assertEqual(str(sp), new_board)


def all_tests():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(PuzzleTest),
    ])

if __name__ == '__main__':

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

