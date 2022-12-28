from django.contrib import admin
from .models import ChessboardModel, GameStateModel
# Register your models here.


admin.site.register(ChessboardModel)
admin.site.register(GameStateModel)
