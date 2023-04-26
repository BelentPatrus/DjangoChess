from django.contrib import admin
from .models import ChessboardModel, GameStateModel, ChessBoardMove
# Register your models here.


# admin.site.register(ChessboardModel)
admin.site.register(GameStateModel)
admin.site.register(ChessBoardMove)


@admin.display(description="GameState Id")
def getGameStateId(obj):
    return obj.id


@admin.register(ChessboardModel)
class chessboardModelAdmin(admin.ModelAdmin):
    list_display = [getGameStateId, "playerTurn", "date"]
