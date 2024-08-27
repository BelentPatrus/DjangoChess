import json
from ..engine.Pieces.Pieces import Pieces
from ..engine.TeamSideE import TeamSideE
from ..helper import Helper
from ..models import ChessBoardModel, ChessMoveModel

from django.db.models import Q

class ChessDB:
    def __init__(self, gameStateID):
        self.gameStateID = gameStateID

    def insertChessboardModel(self, boardJsonDict, moveDict, team):
        moveDictConverted = Helper.convert_keys_to_strings(moveDict)
        chessboardData = ChessBoardModel(
            chessboard=json.dumps(boardJsonDict),
            moveDict=moveDictConverted,
            gameState=self.getGameStateID(),
            playerTurn=team,
        )
        chessboardData.save()

    def insertChessMoveModel(self, moveData):
        chessMoveData = ChessMoveModel(
            piece=moveData["piece"],
            position=moveData["position"],
            move=moveData["move"],
            pieceTaken=moveData["pieceTaken"],
            result=moveData["result"],
            gameState=self.getGameStateID(),
        )
        chessMoveData.save()

    def getKingsFirstMoveQuery(self, team):

        position = [0,4]
        if team == TeamSideE.WHITE:
            position = [7,4]
        try:
            kingMoves = ChessMoveModel.objects.filter(
                gameState=self.getGameStateID(),
                piece__type=Pieces.KING.value,
                piece__team=team,
                position=position
            ).order_by("date")
        except ChessMoveModel.DoesNotExist:
            kingMoves = None

        return kingMoves

    def getMovesDictQuery(self):
        try:
            movesDict = ChessBoardModel.objects.filter(
                gameState=self.getGameStateID(),
            ).values('moveDict').latest('date')
            movesDict = Helper.convert_keys_to_tuples(movesDict['moveDict'])
        except ChessBoardModel.DoesNotExist:
            movesDict = None

        return movesDict

    def updateMovesDictQuery(self, movesDict, jsonDict):
        moveDictConverted = Helper.convert_keys_to_strings(movesDict)
        result = json.dumps(jsonDict)
        chessboardData = ChessBoardModel(
            chessboard=result,
            moveDict=moveDictConverted,
            gameState=self.getGameStateID(),
            playerTurn=self.getPlayerTurn(),
        )
        chessboardData.save()
        return movesDict

    def getRooksFirstMoveQuery(self, team):
        position1 = [7,0]
        position2 = [7,7]
        if team == TeamSideE.WHITE:
            position1 = [0,0]
            position2 = [0,7]
        try:
            firstMovePos1 = ChessMoveModel.objects.filter(
                Q(gameState=self.getGameStateID()) &
                Q(piece__type=Pieces.ROOK.value) &
                Q(piece__team=team) &
                Q(position=position1)
            ).earliest("date")
        except ChessMoveModel.DoesNotExist:
            firstMovePos1 = None

        try:
            firstMovePos2 = ChessMoveModel.objects.filter(
                Q(gameState=self.getGameStateID()) &
                Q(piece__type=Pieces.ROOK.value) &
                Q(piece__team=team) &
                Q(position=position2)
            ).earliest("date")
        except ChessMoveModel.DoesNotExist:
            firstMovePos2 = None

        return firstMovePos1, firstMovePos2

    def saveCastle(self, moveData):
        chessMoveDataKing = ChessMoveModel(
                    piece=moveData['piece'],
                    position=moveData['position'],
                    move=moveData['move'],
                    pieceTaken=moveData['pieceTaken'],
                    result=moveData['result'],
                    gameState=self.getGameStateID()
                )
        chessMoveDataRook = ChessMoveModel(
                    piece=moveData['rookPiece'],
                    position=moveData['rookPosition'],
                    move=moveData['rookMove'],
                    pieceTaken=moveData['rookPieceTaken'],
                    result=moveData['result'],
                    gameState=self.getGameStateID()
                )
        chessMoveDataKing.save()
        chessMoveDataRook.save()

    def getGameStateID(self):
        return self.gameStateID

    def getPlayerTurn(self):
        return self.playerTurn
