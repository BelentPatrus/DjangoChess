
import json

from .Pieces.rook import Rook
from .Pieces.bishop import Bishop
from .Pieces.queen import Queen
from .Pieces.king import King
from .Pieces.knight import Knight
from .Pieces.pawn import Pawn
from .Pieces.empty import Empty
from .Pieces.Pieces import Pieces
from .TeamSideE import TeamSideE
from ..models import ChessboardModel


class Chessboard:

    def __init__(self, chessBoardModel=None):
        if chessBoardModel == None:

            self.board = [

                [Rook(TeamSideE.BLACK, Pieces.ROOK), Knight(TeamSideE.BLACK,  Pieces.KNIGHT), Bishop(TeamSideE.BLACK, Pieces.BISHOP), Queen(TeamSideE.BLACK, Pieces.QUEEN), King(
                    TeamSideE.BLACK, Pieces.KING), Bishop(TeamSideE.BLACK, Pieces.BISHOP), Knight(TeamSideE.BLACK, Pieces.KNIGHT), Rook(TeamSideE.BLACK, Pieces.ROOK)],
                [Pawn(TeamSideE.BLACK, Pieces.PAWN) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Pawn(TeamSideE.WHITE, Pieces.PAWN) for i in range(8)],
                [Rook(TeamSideE.WHITE, Pieces.ROOK), Knight(TeamSideE.WHITE, Pieces.KNIGHT), Bishop(TeamSideE.WHITE, Pieces.BISHOP), Queen(TeamSideE.WHITE, Pieces.QUEEN), King(
                    TeamSideE.WHITE, Pieces.KING), Bishop(TeamSideE.WHITE, Pieces.BISHOP), Knight(TeamSideE.WHITE, Pieces.KNIGHT), Rook(TeamSideE.WHITE, Pieces.ROOK)]
            ]
            self.moveLog = []
            self.captureLog = []
        else:
            self.board = chessBoardModel
            self.moveLog = []  # come back and fix this must query db
            self.captureLog = []  # come back and fix this must query db

    def movePiece(self, cur, next):
        """
            args: move dict with the current and next move location in two lists accessible with key's 'curr' and 'next'
            returns: True or False based on if the move is in the moveset calculated to be in the piece's move list.

        """
        # To test comment and make moveInfo = move
        # moveInfo = json.loads(move)
        # moveInfo = move
        # row, col = moveInfo['curr'][0], moveInfo['curr'][1]
        row, col = cur[0], cur[1]
        moveSet = self.board[row][col].validMoves(self.board, cur)
        isValid = tuple(next) in moveSet
        if isValid:
            # print('Piece: \n{}, \nmoveInfo: \n{}'.format(self.board[row][col], moveInfo['next']))
            self.moveLog.append(
                tuple([self.board[row][col], next]))
            nextRow, nextCol = next[0], next[1]
            # print('In valid if statement changing the pieces position to {},{}'.format(nextRow, nextCol))
            self.board[nextRow][nextCol] = self.board[row][col]
            self.board[row][col] = Empty("Empty", Pieces.EMPTY)
            print('Made move to [{},{}]'.format(nextRow, nextCol))

        return isValid
