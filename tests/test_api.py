from pathlib import Path

import pytest

from meteoalarmpy.api import MeteoAlarm

FIXTURE_DIR = Path(__file__).parent.resolve() / "test_files"


@pytest.mark.datafiles(FIXTURE_DIR)
def test_meteoalarm(mock_fetcher):
    m = MeteoAlarm()
    entries = m.get_entries("poland")
    assert entries is not None
    assert len(entries) > 0


@pytest.mark.datafiles(FIXTURE_DIR)
def test_entries_poland(mock_fetcher):
    country_name = "poland"
    m = MeteoAlarm()
    entries = m.get_entries(country_name)
    parsed_entries = m.get_parsed_entries(country_name)
    assert len(entries) > 0
    assert len(parsed_entries) > 0
