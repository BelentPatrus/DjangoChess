from rest_framework import serializers
from .models import ChessboardModel, ChessBoardMove


class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessboardModel
        fields = '__all__'


class ChessBoardMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessBoardMove
        fields = '__all__'
