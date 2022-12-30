from abc import ABC, abstractmethod
import json
from .Pieces import Pieces


class Piece(ABC):

    def __init__(self, team, type):
        self.team = team
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

        self.type = strType

    @abstractmethod
    def validMoves(self, board, cur):
        """
            args: The state of the board (2d array), the move that wants to be made (dictionary with field 'next' with move values).
            return: list of moves that the piece can make each in a tuple (row, coloumn).
        """
        pass

    def getJSONDict(self):
        return {
            'team': self.team,
            'type': self.type

        }
