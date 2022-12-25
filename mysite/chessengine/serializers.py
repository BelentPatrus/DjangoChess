from rest_framework import serializers
from .models import chessboard


class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = chessboard
        fields = '__all__'
