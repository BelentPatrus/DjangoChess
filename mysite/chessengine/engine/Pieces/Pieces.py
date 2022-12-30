from enum import Enum


class Pieces(str, Enum):
    PAWN = "PAWN"
    BISHOP = "BISHOP"
    EMPTY = "EMPTY"
    KNIGHT = "KNIGHT"
    QUEEN = "QUEEN"
    ROOK = "ROOK"
    KING = "KING"
