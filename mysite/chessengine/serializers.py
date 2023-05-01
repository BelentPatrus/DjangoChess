from rest_framework import serializers
from .models import ChessBoardModel, ChessMoveModel


class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessBoardModel
        fields = '__all__'


class ChessBoardMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessMoveModel
        fields = '__all__'
