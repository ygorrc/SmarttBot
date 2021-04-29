from django.contrib import admin
from django.urls import path

from candles.views import CandlesViewsSets

urlpatterns ={
    path('candles', CandlesViewsSets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('candles/<str:pk>', CandlesViewsSets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
}