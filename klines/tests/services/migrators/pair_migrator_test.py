import pytest
import vcr
from klines.services.migrators.pair_migrator import PairMigrator
from klines.models import Pair

my_vcr = vcr.VCR(
    decode_compressed_response=True,
    cassette_library_dir='fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method']
)


@pytest.mark.django_db
@my_vcr.use_cassette()
def test_pairs_creation():
    PairMigrator().call()

    pairs = Pair.objects.all()

    assert pairs.count() == 2

    # First pair
    pair = pairs[0]

    assert pair.symbol == 'BTCUSDT'
    assert pair.base_asset == 'BTC'
    assert pair.quote_asset == 'USDT'

    # Second pair
    pair = pairs[1]

    assert pair.symbol == 'ETHUSDT'
    assert pair.base_asset == 'ETH'
    assert pair.quote_asset == 'USDT'


@pytest.mark.django_db
@my_vcr.use_cassette('fixtures/cassettes/test_pairs_creation')
def test_pairs_creation_with_existing_pair():
    Pair.objects.create(symbol='BTCUSDT', base_asset='BTC', quote_asset='USDT')

    PairMigrator().call()

    pairs = Pair.objects.all()

    assert pairs.count() == 2

    # First pair
    pair = pairs[0]

    assert pair.symbol == 'BTCUSDT'
    assert pair.base_asset == 'BTC'
    assert pair.quote_asset == 'USDT'

    # Second pair
    pair = pairs[1]

    assert pair.symbol == 'ETHUSDT'
    assert pair.base_asset == 'ETH'
    assert pair.quote_asset == 'USDT'
