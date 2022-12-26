from abc import ABC, abstractmethod
import json
from .Pieces import Pieces


class Piece(ABC, dict):

    
    def __init__(self, team, type):
        self.moves = []
        if type == Pieces.BISHOP:
            strType = "BISHOP"
        elif type == Pieces.PAWN:
            strType = "PAWN"
        elif type == Pieces.QUEEN:
            strType = "QUEEN"
        elif type == Pieces.KNIGHT:
            strType = "KNIGHT"
        elif type == Pieces.KING:
            strType = "KING"
        elif type == Pieces.EMPTY:
            strType = "EMPTY"
        elif type == Pieces.ROOK:
            strType = "ROOK"
        else:
            return

        dict.__init__(self, team=team, type=strType)

    @abstractmethod
    def validMove(self):
        pass
