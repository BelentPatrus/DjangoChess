from django.db import models
# Create your models here.


class GameStateModel(models.Model):
    gameOver = models.BooleanField(default=False)
    playerTurn = models.SlugField(default="WHITE")
    totalMoves = models.PositiveSmallIntegerField(default=0)


class ChessBoardModel(models.Model):
    chessboard = models.JSONField()
    moveDict = models.JSONField(null=True)
    date = models.DateTimeField(auto_now=True)
    playerTurn = models.TextField(max_length=15)
    gameState = models.ForeignKey(GameStateModel, on_delete=models.CASCADE)


class ChessMoveModel(models.Model):
    piece = models.JSONField(default=None) # team: WHITE, type: ROOK
    move = models.JSONField(default=None) # [1,2]
    position = models.JSONField(default=None)  # [0,2]
    pieceTaken = models.JSONField(default=None) # None or team: BLACK, type: PAWN
    result = models.TextField(null=True) # MOVE,TAKE,CASTLE, EN PASSANT
    date = models.DateTimeField(auto_now=True) # Keep track of order
    gameState = models.ForeignKey(GameStateModel, on_delete=models.CASCADE) # search in relation to which game
