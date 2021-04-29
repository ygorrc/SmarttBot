from __future__ import absolute_import, unicode_literals


from celery import shared_task
from poloniex import Poloniex
from datetime import datetime
from candles.models import candle
from candles.serializers import CandlesSerializer
import time
#Tasks onde vai pegar informações poloniex.api e passar o banco de dados de acordo com tempo de cada candle
#chamadas destas task estão no arquivoo senttings.py pelo framework beat
@shared_task
def poloniex_function_1min():
    polo = Poloniex()
    tempo_inicial = time.time()
    tempo_corrido = tempo_inicial
    ticker = polo.returnTicker()['USDC_BTC']['last']
    candle_object = candle()
    candle_object.moeda = 'Bitcoin'
    candle_object.periodicidade = '1min'
    candle_object.datetime = datetime.now()
    candle_object.entrada = ticker
    candle_object.maior = ticker
    candle_object.menor = ticker
    while tempo_corrido - tempo_inicial < 60: 
        ticker = polo.returnTicker()['USDC_BTC']['last']
        if candle_object.maior < ticker:
            candle_object.maior = ticker
        if candle_object.menor > ticker:
            candle_object.menor = ticker
        time.sleep(0.9)
        tempo_corrido = time.time()
    candle_object.saida = ticker
    candle_object.save()
    return 
@shared_task
def poloniex_function_5min():
    polo = Poloniex()
    tempo_inicial = time.time()
    tempo_corrido = tempo_inicial
    ticker = polo.returnTicker()['USDC_BTC']['last']
    candle_object = candle()
    candle_object.moeda = 'Bitcoin'
    candle_object.periodicidade = '5min'
    candle_object.datetime = datetime.now()
    candle_object.entrada = ticker
    candle_object.maior = ticker
    candle_object.menor = ticker
    while tempo_corrido - tempo_inicial < 300: 
        ticker = polo.returnTicker()['USDC_BTC']['last']
        if candle_object.maior < ticker:
            candle_object.maior = ticker
        if candle_object.menor > ticker:
            candle_object.menor = ticker
        time.sleep(0.9)
        tempo_corrido = time.time()
    candle_object.saida = ticker
    candle_object.save()
    return 
@shared_task
def poloniex_function_10min():
    polo = Poloniex()
    tempo_inicial = time.time()
    tempo_corrido = tempo_inicial
    ticker = polo.returnTicker()['USDC_BTC']['last']
    candle_object = candle()
    candle_object.moeda = 'Bitcoin'
    candle_object.periodicidade = '10min'
    candle_object.datetime = datetime.now()
    candle_object.entrada = ticker
    candle_object.maior = ticker
    candle_object.menor = ticker
    while tempo_corrido - tempo_inicial < 600: 
        ticker = polo.returnTicker()['USDC_BTC']['last']
        if candle_object.maior < ticker:
            candle_object.maior = ticker
        if candle_object.menor > ticker:
            candle_object.menor = ticker
        time.sleep(0.9)
        tempo_corrido = time.time()
    candle_object.saida = ticker
    candle_object.save()
    return 