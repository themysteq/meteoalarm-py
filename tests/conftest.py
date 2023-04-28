from pathlib import Path

import pytest

from meteoalarmpy.fetcher import Fetcher

FIXTURE_DIR = Path(__file__).parent.resolve() / "test_files"


@pytest.fixture
def mock_fetcher(datafiles, monkeypatch):
    def mock_xml(*args, **kwargs):
        country_name = kwargs.get("country_name")
        for f in datafiles.iterdir():
            if f.name.endswith(f"{country_name}.xml"):
                with open(f, "r") as xmlfile:
                    data = "\n".join(xmlfile.readlines())
                return data

    monkeypatch.setattr(Fetcher, "_get_raw_xml", mock_xml)
