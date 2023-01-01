
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
from .Pieces.piece import Piece


class Chessboard:

    def __convert2D__(self, board):
        result = []
        row = 8
        index = 0
        while index < len(board):
            result.append(board[index:index+row])
            index = index + row
        return result

    def __init__(self, chessBoardModel=None, playerTurn=TeamSideE.WHITE):
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
            self.playerTurn = playerTurn
        else:
            self.board = []
            for p in chessBoardModel:
                if p['type'] == Pieces.BISHOP:
                    tmp = Bishop(p['team'], Pieces.BISHOP)
                elif p['type'] == Pieces.PAWN:
                    tmp = Pawn(p['team'], Pieces.PAWN)
                elif p['type'] == Pieces.QUEEN:
                    tmp = Queen(p['team'], Pieces.QUEEN)
                elif p['type'] == Pieces.KNIGHT:
                    tmp = Knight(p['team'], Pieces.KNIGHT)
                elif p['type'] == Pieces.KING:
                    tmp = King(p['team'], Pieces.KING)
                elif p['type'] == Pieces.EMPTY:
                    tmp = Empty(p['team'], Pieces.EMPTY)
                elif p['type'] == Pieces.ROOK:
                    tmp = Rook(p['team'], Pieces.ROOK)
                else:
                    return
                self.board.append(tmp)
            self.board = self.__convert2D__(self.board)
            self.moveLog = []  # come back and fix this must query db
            self.captureLog = []  # come back and fix this must query db
            self.playerTurn = playerTurn

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
        selectedP = self.board[row][col]
        print(self.board[row][col])
        if selectedP.team != self.playerTurn:
            print("NOT YOUR TURN")
            return False

        moveSet = self.board[row][col].validMoves(self.board, cur)

        isValid = False if moveSet is None else tuple(next) in moveSet

        if isValid:
            # print('Piece: \n{}, \nmoveInfo: \n{}'.format(self.board[row][col], moveInfo['next']))
            self.moveLog.append(
                tuple([self.board[row][col], next]))
            nextRow, nextCol = next[0], next[1]
            # print('In valid if statement changing the pieces position to {},{}'.format(nextRow, nextCol))
            self.board[nextRow][nextCol] = self.board[row][col]
            self.board[row][col] = Empty("Empty", Pieces.EMPTY)
            print('Made move to [{},{}]'.format(nextRow, nextCol))
            self.toggleTurn()

        print("PLAYER TURN IS NOW " + self.playerTurn)
        return isValid

    def getJSONDict(self):
        # need to serialize the board
        chessboardSerialized = []

        for row in self.board:
            for p in row:
                chessboardSerialized.append(p.getJSONDict())

        return chessboardSerialized

    def toggleTurn(self):
        self.playerTurn = TeamSideE.BLACK if self.playerTurn == TeamSideE.WHITE else TeamSideE.WHITE
        return
