
from .piece import Piece


class Rook(Piece):

    def __init__(self, team, type):
        super().__init__(team, type)

    def validMove(self):
        pass
