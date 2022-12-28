from django.db import models
# Create your models here.


class GameStateModel(models.Model):
    gameOver = models.BooleanField(default=False)
    playerTurn = models.SlugField(default="WHITE")
    selectedPieceCordinates = models.CharField(null=True, max_length=15)
    moveToCordinates = models.CharField(null=True, max_length=15)
    totalMoves = models.PositiveSmallIntegerField(default=0)


class ChessboardModel(models.Model):
    chessboard = models.JSONField()
    gameState = models.ForeignKey(GameStateModel, on_delete=models.CASCADE)
