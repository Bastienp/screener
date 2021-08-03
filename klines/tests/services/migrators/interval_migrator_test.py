import pytest
from klines.services.migrators.interval_migrator import IntervalMigrator
from klines.models import Interval

@pytest.mark.django_db
def test_intervals_creation():
    IntervalMigrator().call()

    intervals = Interval.objects.all()
    array_symbols = []
    for interval in intervals:
        array_symbols.append(interval.symbol)

    assert Interval.objects.all().count() == 9
    assert array_symbols == ['1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w']

@pytest.mark.django_db
def test_intervals_creation_with_existing_interval():
    Interval.objects.create(symbol='1h')

    IntervalMigrator().call()

    intervals = Interval.objects.all()
    array_symbols = []
    for interval in intervals:
        array_symbols.append(interval.symbol)

    assert Interval.objects.all().count() == 9
    assert array_symbols == ['1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w']