from rest_framework import serializers
from .models import ChessboardModel


class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessboardModel
        fields = '__all__'
