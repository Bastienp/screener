import pytest
import vcr
from klines.services.fetch_klines import FetchKlines
from klines.models import Kline
from klines.models import Pair
from klines.models import Interval
from freezegun import freeze_time

my_vcr = vcr.VCR(
    decode_compressed_response=True,
    cassette_library_dir='fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method']
)

@pytest.mark.django_db
@my_vcr.use_cassette()
@freeze_time("2021-08-03 14:12:12")
def test_fetch_klines():
    btc_usdt_pair = Pair.objects.create(symbol='BTCUSDT', base_asset='BTC', quote_asset='USDT')
    weekly_interval = Interval.objects.create(symbol='1w')

    FetchKlines.call('BTCUSDT', '1w', 1626652800000)

    klines = Kline.objects.all()

    assert klines.count() == 3

    kline = klines[0]

    assert kline.pair == btc_usdt_pair
    assert kline.interval == weekly_interval
    assert kline.interval == weekly_interval
