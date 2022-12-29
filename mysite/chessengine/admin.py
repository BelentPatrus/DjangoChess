from django.contrib import admin
from .models import ChessboardModel, GameStateModel, ChessBoardMove
# Register your models here.


admin.site.register(ChessboardModel)
admin.site.register(GameStateModel)
admin.site.register(ChessBoardMove)
