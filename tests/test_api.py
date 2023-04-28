from meteoalarmpy.api import MeteoAlarm


def test_meteoalarm():
    m = MeteoAlarm()
    entries = m.get_entries('Poland')
    assert entries is not None
    assert len(entries) > 0
