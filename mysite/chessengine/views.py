
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import chessboard
from .serializers import ChessboardSerializer

# Create your views here.


@api_view(['GET'])
def getData(request):
    data = chessboard.objects.all()[0]

    # serializer = ChessboardSerializer(chessboard, many=False)

    return Response(data.chessboardSetup)

    # person = [
    #     {

    #         "type": "rook",
    #         "color": "black",
    #     },
    #     {
    #         "type": "bishop",
    #         "color": "black",
    #     },
    #     {
    #         "type": "horse",
    #         "color": "black",
    #     },
    #     {
    #         "type": "bishop",
    #         "color": "black",
    #     },
    #     {
    #         "type": "queen",
    #         "color": "black",
    #     },
    #     {
    #         "type": "king",
    #         "color": "black",
    #     },
    #     {
    #         "type": "bishop",
    #         "color": "black",
    #     },
    #     {
    #         "type": "horse",
    #         "color": "black",
    #     },
    #     {
    #         "type": "rook",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },
    #     {
    #         "type": "pawn",
    #         "color": "black",
    #     },

    # ]
