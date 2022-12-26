
from .engine.chessboard import Chessboard

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import chessboard
from .serializers import ChessboardSerializer
import json

# Create your views here.


@api_view(['GET'])
def getData(request):
    startBoard = Chessboard("white", "black")
#    # data = chessboard.objects.all()[0]
    # data = [{"type": "rook", "color": "black"}, {"type": "horse", "color": "black"}, {"type": "bishop", "color": "black"}, {"type": "queen", "color": "black"}, {"type": "king", "color": "black"}, {"type": "bishop", "color": "black"}, {"type": "horse", "color": "black"}, {"type": "rook", "color": "black"}, {
    # "type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}, {"type": "pawn", "color": "black"}]
    result = json.dumps(startBoard.board)
    taskdata = chessboard(chessboardSetup=result)

    taskdata.save()
    data = chessboard.objects.all()[2]
    serializer = ChessboardSerializer(data, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    startBoard = Chessboard("white", "black")
