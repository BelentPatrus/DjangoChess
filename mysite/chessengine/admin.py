from django.contrib import admin
from .models import ChessBoardModel, GameStateModel, ChessMoveModel
# Register your models here.


# admin.site.register(ChessboardModel)
admin.site.register(GameStateModel)
admin.site.register(ChessMoveModel)


@admin.display(description="GameState Id")
def getGameStateId(obj):
    return obj.id


@admin.register(ChessBoardModel)
class chessboardModelAdmin(admin.ModelAdmin):
    list_display = [getGameStateId, "playerTurn", "date"]
