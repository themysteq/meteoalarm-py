import datetime
import logging
from pathlib import Path

import pytest

from meteoalarmpy.api import MeteoAlarm
from meteoalarmpy.models import cap_types

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
    assert len(entries) == 2
    assert len(parsed_entries) == 2


@pytest.mark.datafiles(FIXTURE_DIR)
def test_entries_poland_eastern_coastal_zone_meteo(mock_fetcher):
    country_name = "poland"
    m = MeteoAlarm()
    entries = m.get_entries(country_name)
    eastern_coastal_zone_entry = entries[0]
    assert (
        eastern_coastal_zone_entry.cap__message_type == cap_types.CAPMessageType.ALERT
    )
    assert eastern_coastal_zone_entry.cap__scope == cap_types.CAPScope.PUBLIC
    assert eastern_coastal_zone_entry.cap__certainty == cap_types.CAPCertainty.LIKELY
    assert eastern_coastal_zone_entry.cap__urgency == cap_types.CAPUrgency.EXPECTED
    assert eastern_coastal_zone_entry.cap__status == cap_types.CAPStatus.ACTUAL
    assert eastern_coastal_zone_entry.cap__severity == cap_types.CAPSeverity.MODERATE
    assert eastern_coastal_zone_entry.cap__onset.date() == datetime.date(2023, 4, 27)


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
    assert len(entries) == len(parsed_entries)
    assert len(parsed_entries) > 0
