

from .Pieces.Pawn import Pawn
from .Pieces.Rook import Rook
from .Pieces.King import King
from .Pieces.Knight import Knight
from .Pieces.Bishop import Bishop
from .Pieces.Queen import Queen
from .Pieces.Empty import Empty
from .Pieces.Pieces import Pieces


class Chessboard:
    def __init__(self, colour_white, colour_black):
        self.board = [
            [Rook(colour_black, Pieces.ROOK), Knight(colour_black,  Pieces.KNIGHT), Bishop(colour_black, Pieces.BISHOP), Queen(colour_black, Pieces.QUEEN), King(
                colour_black, Pieces.KING), Bishop(colour_black, Pieces.BISHOP), Knight(colour_black, Pieces.KNIGHT), Rook(colour_black, Pieces.ROOK)],
            [Pawn(colour_black, Pieces.PAWN) for i in range(8)],
            [Empty("Empty", Pieces.EMPTY) for i in range(8)],
            [Empty("Empty", Pieces.EMPTY) for i in range(8)],
            [Empty("Empty", Pieces.EMPTY) for i in range(8)],
            [Empty("Empty", Pieces.EMPTY) for i in range(8)],
            [Pawn(colour_white, Pieces.PAWN) for i in range(8)],
            [Rook(colour_white, Pieces.ROOK), Knight(colour_white, Pieces.KNIGHT), Bishop(colour_white, Pieces.BISHOP), King(colour_white, Pieces.KING), Queen(
                colour_white, Pieces.QUEEN), Bishop(colour_white, Pieces.BISHOP), Knight(colour_white, Pieces.KNIGHT), Rook(colour_white, Pieces.ROOK)]
        ]
