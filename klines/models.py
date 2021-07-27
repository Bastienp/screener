from django.db import models

class Pair(models.Model):
    symbol = models.CharField(max_length=40, unique=True)
    base_asset = models.CharField(max_length=20)
    quote_asset = models.CharField(max_length=20)

    def __str__(self):
        return self.symbol

class Interval(models.Model):
    symbol = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.symbol

class Kline(models.Model):
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE, null=True)
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE, null=True)
    opened_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    open_price = models.DecimalField(max_digits=19, decimal_places=8)
    high_price = models.DecimalField(max_digits=19, decimal_places=8)
    low_price = models.DecimalField(max_digits=19, decimal_places=8)
    close_price = models.DecimalField(max_digits=19, decimal_places=8)
    volume = models.DecimalField(max_digits=19, decimal_places=8)
    quote_volume = models.DecimalField(max_digits=19, decimal_places=8)
    taker_buy_base_volume = models.DecimalField(max_digits=19, decimal_places=8)
    taker_buy_quote_volume = models.DecimalField(max_digits=19, decimal_places=8)
