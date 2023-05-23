import logging
from pathlib import Path

import pytest

from meteoalarmpy.api import MeteoAlarm

FIXTURE_DIR = Path(__file__).parent.resolve() / "test_files"
logger = logging.getLogger(__name__)
# XML local files based


@pytest.mark.datafiles(FIXTURE_DIR)
def test_meteoalarm(mock_fetcher):
    m = MeteoAlarm()
    entries = m.get_raw_entries("poland")
    assert entries is not None
    assert len(entries) > 0


@pytest.mark.datafiles(FIXTURE_DIR)
def test_entries_poland(mock_fetcher):
    country_name = "poland"
    m = MeteoAlarm()
    entries = m.get_raw_entries(country_name)
    parsed_entries = m.get_entries(country_name)
    assert len(entries) > 0
    assert len(parsed_entries) > 0


# vcr-py based


@pytest.mark.vcr()
def test_entries_poland_api():
    country_name = "poland"
    m = MeteoAlarm()
    entries = m.get_raw_entries(country_name)
    parsed_entries = m.get_entries(country_name)
    logger.info(
        f"entries for '{country_name}' is: parsed={len(parsed_entries)}, raw={len(entries)}"
    )
    assert len(entries) > 0
    assert len(parsed_entries) > 0
