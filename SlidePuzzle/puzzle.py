from aenum import Enum

__author__ = 'Jason Cozens'

message = "WELCOME TO SLIDING PUZZLES!"


class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4


class SlidePuzzle:

    Width = 3
    Height = 3

    def __init__(self):
        self._board = {}
        for y in range(1, SlidePuzzle.Height + 1):
            for x in range(1, SlidePuzzle.Width + 1):
                self._board[(x, y)] = (y - 1) * 3 + x
        self._board[(3, 3)] = 0

    def __str__(self):
        board = ""
        for y in range(1, SlidePuzzle.Height + 1):
            board += "| "
            for x in range(1, SlidePuzzle.Width + 1):
                if self._board[(x, y)] == 0:
                    board += "  | "
                else:
                    board += str(self._board[(x, y)]) + " | "
            board = board.rstrip(' ')
            board += '\n'
        board = board.rstrip('\n')
        return board

    def can_move(self, tile):
        xy = [key for key, value in self._board.items() if value == tile][0]
        zero = [key for key, value in self._board.items() if value == 0][0]
        (zx, zy) = zero
        return xy in {(zx - 1, zy), (zx, zy - 1), (zx + 1, zy), (zx, zy + 1)}

    def move(self, tile):
        if self.can_move(tile):
            xy = [key for key, value in self._board.items() if value == tile][0]
            zero = [key for key, value in self._board.items() if value == 0][0]
            self._board[xy] = 0
            self._board[zero] = tile

    def move_space(self, direction):
        (zx, zy) = [key for key, value in self._board.items() if value == 0][0]
        if direction == Direction.Left:
            if zx > 1:
                self._board[(zx, zy)] = self._board[(zx - 1, zy)]
                self._board[(zx - 1, zy)] = 0
        if direction == Direction.Right:
            if zy < SlidePuzzle.Width:
                self._board[(zx, zy)] = self._board[(zx + 1, zy)]
                self._board[(zx + 1, zy)] = 0
        if direction == Direction.Up:
            if zy > 1:
                self._board[(zx, zy)] = self._board[(zx, zy - 1)]
                self._board[(zx, zy - 1)] = 0
        if direction == Direction.Down:
            if zy < SlidePuzzle.Height:
                self._board[(zx, zy)] = self._board[(zx, zy + 1)]
                self._board[(zx, zy + 1)] = 0
