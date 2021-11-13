from binance import Client
from klines.models import Kline
from klines.models import Pair
from klines.models import Interval
from datetime import datetime
from django.utils.timezone import make_aware
import environ

env = environ.Env()
environ.Env.read_env()

class FetchKlines:

    @staticmethod
    def call(symbol, interval_symbol, start_time):
        client = Client(env('BINANCE_API_USERNAME'), env('BINANCE_API_PASSWORD'))
        klines = client.get_historical_klines(symbol, interval_symbol, start_time)
        pair = Pair.objects.get(symbol=symbol)
        interval = Interval.objects.get(symbol=interval_symbol)

        for kline in klines:
            Kline.objects.create(
                pair=pair,
                interval=interval,
                opened_at=make_aware(datetime.fromtimestamp(kline[0] / 1000)),
                open_price=kline[1],
                high_price=kline[2],
                low_price=kline[3],
                close_price=kline[4],
                volume=kline[5],
                closed_at=make_aware(datetime.fromtimestamp(kline[6] / 1000)),
                quote_volume=kline[7],
                taker_buy_base_volume=kline[8],
                taker_buy_quote_volume=kline[9]
            )
