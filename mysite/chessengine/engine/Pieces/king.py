from .piece import Piece


class King(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

    def validMoves(self):
        pass