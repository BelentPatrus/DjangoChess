from rest_framework import serializers
from .models import ChessBoardModel, ChessBoardMove


class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessBoardModel
        fields = '__all__'


class ChessBoardMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessBoardMove
        fields = '__all__'
