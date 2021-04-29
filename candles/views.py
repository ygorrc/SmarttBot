from django.shortcuts import render
from django_mysql import status
from rest_framework.response import Response
from rest_framework import viewsets,status

from candles.models import candle
from candles.serializers import CandlesSerializer


class CandlesViewsSets(viewsets.ViewSet):
    def list(self, request):
        candles = candle.objects.all()
        serializer = CandlesSerializer(candles,many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = CandlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(selfs, request, pk=None):
        candles = candle.objects.get(id=pk)
        serializer = CandlesSerializer(candles)
        return Response(serializer.data)

    def update(self, request, pk=None):
        candles = candle.objects.get(id=pk)
        serializer = CandlesSerializer(instance=candles, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self, request, pk=None):
        candles = candle.objects.get(id=pk)
        candles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
