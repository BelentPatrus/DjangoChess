from django.contrib import admin
from .models import ChessBoardModel, GameStateModel, ChessMoveModel
# Register your models here.


# admin.site.register(ChessboardModel)
# admin.site.register(GameStateModel)
# admin.site.register(ChessMoveModel)


@admin.display(description="GameState Id")
def getGameStateId(obj):
    return obj.id


@admin.register(ChessBoardModel)
class ChessBoardModelAdmin(admin.ModelAdmin):
    list_display = [getGameStateId, "playerTurn", "date"]


@admin.register(GameStateModel)
class GameStateModelAdmin(admin.ModelAdmin):
    list_display = ["id", "totalMoves", "playerTurn", "gameOver"]


@admin.register(ChessMoveModel)
class ChessMoveModelAdmin(admin.ModelAdmin):
    list_display = [getGameStateId, "cords", "result", "date"]
