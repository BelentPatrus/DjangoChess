from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .engine.chessboard import Chessboard
from chessengine.engine.Pieces.empty import Empty
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChessBoardModel, GameStateModel, ChessMoveModel
from .serializers import ChessboardSerializer, ChessBoardMoveSerializer
from .engine.chessboard import Chessboard
from .engine.TeamSideE import TeamSideE
from .forms import RegisterForm, LoginForm
from .helper import Helper
from .datalayer.ChessDB import ChessDB
import json


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/new")
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "registration/login.html", context)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # username = form.cleaned_data.get("username")
            # messages.success(request, f"Account created for {username}!")
            return redirect("/new")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "registration/sign_up.html", context)


def logout(request):
    logout(request)
    return redirect("login")


@api_view(["GET"])
def getLatestChessBoardData(request, gameStateId):
    data = ChessBoardModel.objects.all().filter(gameState=gameStateId).latest("date")
    serializer = ChessboardSerializer(data, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getData(request):
    gameStateData = GameStateModel.objects.create()

    startBoard = Chessboard()
    movesDict = startBoard.getAllValidMoves()
    moveDictConverted = Helper.convert_keys_to_strings(movesDict)

    result = json.dumps(startBoard.getJSONDict())

    chessboardData = ChessBoardModel(
        chessboard=result, moveDict=moveDictConverted, gameState=gameStateData, playerTurn=TeamSideE.WHITE
    )

    chessboardData.save()
    data = ChessBoardModel.objects.filter(gameState=gameStateData).latest("date")
    serializer = ChessboardSerializer(data, many=False)
    print(serializer.data)

    return Response(serializer.data)


def twoPointMove(request):
    data = {}
    serializer = ChessBoardMoveSerializer(data=request.data)
    if serializer.is_valid():
        print("======================serial data============================")
        print(serializer.validated_data)

        gameStateId = serializer.validated_data.get("gameState")
        chessboardModelData = (
            ChessBoardModel.objects.all().filter(gameState=gameStateId).latest("date")
        )

        playerTurn = chessboardModelData.playerTurn
        chessboard = Chessboard(json.loads(chessboardModelData.chessboard), playerTurn, gameStateId)
        position = json.loads(serializer.validated_data.get("position"))
        move = json.loads(serializer.validated_data.get("move"))
        print(position)
        print(move)
        position[0] -= 1
        position[1] -= 1
        move[0] -= 1
        move[1] -= 1
        if (
            chessboard.board[position[0]][position[1]].team.lower()
            == chessboard.board[move[0]][move[1]].team.lower()
        ):
            data["sameTeam"] = True
            data["data"] = serializer.data
            return data

        movePieceResult = chessboard.movePiece(position, move)

        if movePieceResult['isValid']:
            data["sameTeam"] = False

    else:
        print(request.data)
        print(serializer.errors)

    data["data"] = serializer.data
    return data


@csrf_exempt
def chessMatch(request, match_id):
    rangeset = range(1, 9)
    context = {"range": rangeset, "match_id": match_id}
    return render(request, "chessMatch.html", context)


def lobby(request):
    rangeset = range(1, 9)
    context = {
        "range": rangeset,
    }
    return render(request, "lobby.html", context)


@api_view(["GET", "POST"])
def processClick(request):
    """
    This function will process the click of a user determining which action to take regarding these situations:
    1. Piece Clicked : returns the highlighted moves arr if playerTurn clicked their piece.
    2. Move Piece : makes move on chess board
    """
    move = request.data.get("move", None)
    if move:
        moveDict = twoPointMove(request)
        moveDict["Operation"] = "move"
        return Response(moveDict)
    else:
        highlightDict = getAvailableMoves(request)
        highlightDict["Operation"] = "highlight"
        return Response(highlightDict)

    print(
        f"ProcessClick: {request.data}"
    )

def getAvailableMoves(request):
    # Get available moves for the chess piece in question

    gameStateId = request.data["gameState"]
    chessboardModelData = (
        ChessBoardModel.objects.all().filter(gameState=gameStateId).latest("date")
    )

    playerTurn = chessboardModelData.playerTurn
    chessboard = Chessboard(json.loads(chessboardModelData.chessboard), playerTurn, gameStateId)
    position = json.loads(request.data["position"])
    position[0] -= 1
    position[1] -= 1
    team = chessboard.board[position[0]][position[1]].getTeam().value
    chessDB = ChessDB(gameStateId)
    movesDict = chessDB.getMovesDictQuery()
    if not movesDict:
        movesDict = chessboard.updateMovesDictQuery()
    
    moveSet = movesDict[team][tuple(position)]

    moveSetList = []
    for move in moveSet:
        for i in range(len(move)):
            move[i] += 1
        moveSetList.append(move)
    data = {"moveSet": moveSetList}

    return data
