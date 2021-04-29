from rest_framework import serializers

from .models import candle


class CandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = candle
        fields = '__all__'
