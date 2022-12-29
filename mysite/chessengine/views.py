
from django.views.decorators.csrf import csrf_exempt
from .engine.chessboard import Chessboard

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChessboardModel, GameStateModel
from .serializers import ChessboardSerializer, ChessBoardMoveSerializer
import json

# Create your views here.


@api_view(['GET'])
def getData(request):
    gameStateData = GameStateModel.objects.create()

    startBoard = Chessboard("white", "black")

    result = json.dumps(startBoard.board)
    chessboardData = ChessboardModel(
        chessboard=result, gameState=gameStateData)

    chessboardData.save()
    data = ChessboardModel.objects.all()[0]
    serializer = ChessboardSerializer(data, many=False)

    return Response(serializer.data)


@api_view(['POST', 'GET'])
@csrf_exempt
def postData(request):
    serializer = ChessBoardMoveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(request.data)
        print("HHHHHHHHHHHHHHHHHHEYOOOOOOOOOOOOOOOOOOOOOOOO")

    return Response(serializer.data)
