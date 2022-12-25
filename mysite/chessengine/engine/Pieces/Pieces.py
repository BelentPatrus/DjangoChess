from enum import Enum


class Pieces(str, Enum):
    PAWN = 1
    BISHOP = 2
    EMPTY = 3
    KNIGHT = 4
    QUEEN = 5
    ROOK = 6
    KING = 7
