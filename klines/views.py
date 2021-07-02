from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import KlineSerializer
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import environ
env = environ.Env()
environ.Env.read_env()


# Create your views here.

class KlineView(viewsets.ViewSet):
    def list(self, request):
        client = Client(env('BINANCE_API_USERNAME'), env('BINANCE_API_PASSWORD'))
        klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        klines_object = {"klines": klines}
        serializer = KlineSerializer(klines_object, many=False)
        return Response(serializer.data)
