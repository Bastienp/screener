from binance import Client
from klines.models import Pair
import environ

env = environ.Env()
environ.Env.read_env()

class PairMigrator:

    @staticmethod
    def call():
        client = Client(env('BINANCE_API_USERNAME'), env('BINANCE_API_PASSWORD'))
        exchange_info = client.get_exchange_info()
        symbols = exchange_info['symbols']
        usdt_pairs = [pair for pair in symbols if pair['quoteAsset'] == 'USDT']

        for usdt_pair in usdt_pairs:
            if not Pair.objects.filter(symbol=usdt_pair['symbol']).exists():
                Pair.objects.create(symbol=usdt_pair['symbol'], base_asset=usdt_pair['baseAsset'], quote_asset=usdt_pair['quoteAsset'])