
from django.views.decorators.csrf import csrf_exempt
from .engine.chessboard import Chessboard
from chessengine.engine.Pieces.empty import Empty

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChessboardModel, GameStateModel
from .serializers import ChessboardSerializer, ChessBoardMoveSerializer
from .engine.chessboard import Chessboard
from .engine.TeamSideE import TeamSideE
import json

# Create your views here.


@api_view(['GET'])
def getLatestChessBoardData(request, gameStateId):
    data = ChessboardModel.objects.all().filter(
        gameState=gameStateId).latest('date')
    serializer = ChessboardSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getData(request):
    gameStateData = GameStateModel.objects.create()

    startBoard = Chessboard()

    result = json.dumps(startBoard.getJSONDict())

    chessboardData = ChessboardModel(
        chessboard=result, gameState=gameStateData, playerTurn=TeamSideE.WHITE)

    chessboardData.save()
    data = ChessboardModel.objects.filter(
        gameState=gameStateData).latest('date')
    serializer = ChessboardSerializer(data, many=False)

    return Response(serializer.data)


@api_view(['POST', 'GET'])
def twoPointMove(request):
    serializer = ChessBoardMoveSerializer(data=request.data)
    # what i need is to query this data to find latest chessboard related to this datas foreign key
    if serializer.is_valid():
        print("======================serial data============================")
        print(serializer.validated_data)
        # get gamestate id
        # get latest gameboard
        # create ChhessBoard based on latest
        # get cur and next arrays
        # check if valid move

        gameStateId = serializer.validated_data.get('gameState')
        chessboardModelData = ChessboardModel.objects.all().filter(
            gameState=gameStateId).latest('date')
        playerTurn = chessboardModelData.playerTurn
        chessboard = Chessboard(json.loads(
            chessboardModelData.chessboard), playerTurn)
        cur = json.loads(serializer.validated_data.get('selectedPiece'))
        next = json.loads(serializer.validated_data.get('moveLocation'))
        print(cur)
        cur[0] -= 1
        cur[1] -= 1
        next[0] -= 1
        next[1] -= 1
        if chessboard.movePiece(cur, next):
            chessboardData = ChessboardModel(
                chessboard=json.dumps(chessboard.getJSONDict()), gameState=gameStateId, playerTurn=chessboard.playerTurn)
            chessboardData.save()
            serializer.save()

    else:
        print(request.data)
        print("here")

    return Response(serializer.data)

@api_view(['POST','GET'])
def getAvailableMoves(request):
    # Get available moves for the chess piece in question
    
    gameStateId = request.data['gameState']  
    chessboardModelData = ChessboardModel.objects.all().filter(
        gameState=gameStateId).latest('date')
    playerTurn = chessboardModelData.playerTurn
    chessboard= Chessboard(json.loads(chessboardModelData.chessboard), playerTurn)
    position= json.loads(request.data['pieceLocation'])
    position[0] -=1
    position[1] -=1
    moveSet = chessboard.getPieceMoves(position)

    for move in moveSet:
        for i in range(len(move)):
            move[i] += 1
    data = {
        'moveSet' : moveSet
    }
    return Response(data)
        
        
        



    

