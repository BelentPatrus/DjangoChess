from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .engine.chessboard import Chessboard
from chessengine.engine.Pieces.empty import Empty
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChessBoardModel, GameStateModel
from .serializers import ChessboardSerializer, ChessBoardMoveSerializer
from .engine.chessboard import Chessboard
from .engine.TeamSideE import TeamSideE
from .forms import RegisterForm, LoginForm
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

    result = json.dumps(startBoard.getJSONDict())

    chessboardData = ChessBoardModel(
        chessboard=result, gameState=gameStateData, playerTurn=TeamSideE.WHITE
    )

    chessboardData.save()
    data = ChessBoardModel.objects.filter(gameState=gameStateData).latest("date")

    serializer = ChessboardSerializer(data, many=False)

    return Response(serializer.data)


def twoPointMove(request):
    data = {}
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

        gameStateId = serializer.validated_data.get("gameState")
        chessboardModelData = (
            ChessBoardModel.objects.all().filter(gameState=gameStateId).latest("date")
        )

        playerTurn = chessboardModelData.playerTurn
        chessboard = Chessboard(json.loads(chessboardModelData.chessboard), playerTurn)
        cur = json.loads(serializer.validated_data.get("cords"))[0]
        next = json.loads(serializer.validated_data.get("cords"))[1]
        print(cur)
        cur[0] -= 1
        cur[1] -= 1
        next[0] -= 1
        next[1] -= 1
        if (
            chessboard.board[cur[0]][cur[1]].team.lower()
            == chessboard.board[next[0]][next[1]].team.lower()
        ):
            data["sameTeam"] = True
        elif chessboard.movePiece(cur, next):
            chessboardData = ChessBoardModel(
                chessboard=json.dumps(chessboard.getJSONDict()),
                gameState=gameStateId,
                playerTurn=chessboard.playerTurn,
            )
            chessboardData.save()
            serializer.save()
            data["sameTeam"] = False

    else:
        print(request.data)
        print("here")
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
    numClicks = len(json.loads(request.data["cords"]))
    if numClicks == 2:
        moveDict = twoPointMove(request)
        moveDict["Operation"] = "move"
        return Response(moveDict)

    elif numClicks == 1:
        highlightDict = getAvailableMoves(request)
        highlightDict["Operation"] = "highlight"
        return Response(highlightDict)

    print(
        f"Wasn't caught by any of the if statements UserClicks: {request.data['cords']}, Length: {request.data['cords']}"
    )


def getAvailableMoves(request):
    # Get available moves for the chess piece in question

    gameStateId = request.data["gameState"]
    chessboardModelData = (
        ChessBoardModel.objects.all().filter(gameState=gameStateId).latest("date")
    )
    playerTurn = chessboardModelData.playerTurn
    chessboard = Chessboard(json.loads(chessboardModelData.chessboard), playerTurn)
    position = json.loads(request.data["cords"])[0]
    position[0] -= 1
    position[1] -= 1
    moveSet = chessboard.getPieceMoves(position)
    moveSetList = []
    for move in moveSet:
        move = list(move)
        for i in range(len(move)):
            move[i] += 1
        moveSetList.append(move)
    data = {"moveSet": moveSetList}

    return data
