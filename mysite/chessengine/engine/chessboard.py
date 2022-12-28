
import json

from .Pieces.rook import Rook
from .Pieces.bishop import Bishop
from .Pieces.queen import Queen
from .Pieces.king import King
from .Pieces.knight import Knight
from .Pieces.pawn import Pawn
from .Pieces.empty import Empty
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
            [Rook(colour_white, Pieces.ROOK), Knight(colour_white, Pieces.KNIGHT), Bishop(colour_white, Pieces.BISHOP), Queen(colour_white, Pieces.QUEEN), King(
                colour_white, Pieces.KING), Bishop(colour_white, Pieces.BISHOP), Knight(colour_white, Pieces.KNIGHT), Rook(colour_white, Pieces.ROOK)]
        ]
        self.moveLog = []
        self.captureLog = []

    def movePiece(self, move):
        """
            args: move dict with the current and next move location in two lists accessible with key's 'curr' and 'next'
            returns: True or False based on if the move is in the moveset calculated to be in the piece's move list.

        """
        # To test comment and make moveInfo = move
        moveInfo = json.loads(move)
        row, col = moveInfo['curr'][0], moveInfo['curr'][1]
        moveSet = self.board[row][col].validMoves(self.board, moveInfo['curr'])
        isValid = tuple(moveInfo['next']) in moveSet
        if isValid:
            print('Piece: \n{}, \nmoveInfo: \n{}'.format(self.board[row][col], moveInfo['next']))
            self.moveLog.append(tuple([self.board[row][col], moveInfo['next']]))
            nextRow, nextCol = moveInfo['next'][0], moveInfo['next'][1] 
            print('In valid if statement changing the pieces position to {},{}'.format(nextRow, nextCol))  
            self.board[nextRow][nextCol] = self.board[row][col]
            self.board[row][col] = Empty("Empty", Pieces.EMPTY)
        
        return isValid
        
        

