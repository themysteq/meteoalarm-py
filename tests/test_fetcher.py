import pytest

from meteoalarmpy.fetcher import Fetcher


@pytest.mark.vcr()
def test_fetcher():
    fe = Fetcher()
    result = fe.get_xml("Poland")
    assert result is not None
