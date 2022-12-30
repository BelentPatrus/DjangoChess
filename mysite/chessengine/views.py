
from django.views.decorators.csrf import csrf_exempt
from .engine.chessboard import Chessboard

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChessboardModel, GameStateModel
from .serializers import ChessboardSerializer, ChessBoardMoveSerializer
from .engine.chessboard import Chessboard
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
        chessboard=result, gameState=gameStateData)

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
        latestChessboard = ChessboardModel.objects.all().filter(
            gameState=gameStateId).latest('date').chessboard
        chessboard = Chessboard(json.loads(latestChessboard))
        cur = json.loads(serializer.validated_data.get('selectedPiece'))
        next = json.loads(serializer.validated_data.get('moveLocation'))
        print(cur)
        cur[0] -= 1
        cur[1] -= 1
        next[0] -= 1
        next[1] -= 1
        if chessboard.movePiece(cur, next):
            print("=========================================")
            print(chessboard.board)

            chessboardData = ChessboardModel(
                chessboard=chessboard.getJSONDict(), gameState=gameStateId)

            chessboardData.save()
            print("=========================================")

            serializer.save()

    else:
        print(request.data)
        print("here")

    return Response(serializer.data)
