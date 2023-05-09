from abc import ABC, abstractmethod
import json
from .FEN import FEN
from .Pieces import Pieces
from ..TeamSideE import TeamSideE


class Piece(ABC):

    def __init__(self, team, type):
        self.team = team
        self.type = type

    @ abstractmethod
    def validMoves(self, board, cur):
        """
            args: The state of the board (2d array), the move that wants to be made (dictionary with field 'next' with move values).
            return: list of moves that the piece can make each in a tuple (row, coloumn).
        """
        pass

    def getJSONDict(self):
        team = self.team
        type = self.type
        return FEN.encryptFEN(self, team, type)
