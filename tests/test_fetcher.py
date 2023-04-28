from meteoalarmpy.fetcher import Fetcher


def test_fetcher():
    fe = Fetcher()
    result = fe.get_xml("Poland")
    assert result is not None
