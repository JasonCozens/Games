__author__ = 'Jason Cozens'

message = "WELCOME TO SLIDING PUZZLES!"


class SlidePuzzle:

    def __init__(self):
        self._board = {}
        for y in range(1, 4):
            for x in range(1, 4):
                self._board[(x, y)] = (y - 1) * 3 + x
        self._board[(3, 3)] = 0

    def __str__(self):
        board = ""
        for y in range(1, 4):
            board += "| "
            for x in range(1, 4):
                if self._board[(x, y)] == 0:
                    board += "  | "
                else:
                    board += str(self._board[(x, y)]) + " | "
            board = board.rstrip(' ')
            board += '\n'
        board = board.rstrip('\n')
        return board

    def can_move(self, param):
        xy = [key for key, value in self._board.items() if value == param][0]
        zero = [key for key, value in self._board.items() if value == 0][0]
        (zx, zy) = zero
        return xy in {(zx - 1, zy), (zx, zy - 1), (zx + 1, zy), (zx, zy + 1)}

    def move(self, param):
        pass
