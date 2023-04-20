from meteoalarmpy import api


def test_null_function():
    result = api.null_function()
    assert result is True
