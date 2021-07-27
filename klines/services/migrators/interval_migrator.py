from klines.models import Interval


class IntervalMigrator:

    @staticmethod
    def call():
        symbols = ['1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w']

        for symbol in symbols:
            if not Interval.objects.filter(symbol=symbol).exists():
                Interval.objects.create(symbol=symbol)
