import logging
import xml.etree.ElementTree
from typing import List

from .fetcher import Fetcher
from .models.meteoalarmentry import MeteoalarmEntry


class MeteoAlarm:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.fetcher = Fetcher()
        self.xml_namespace = Fetcher.NAMESPACES

    def get_raw_entries(self, country_name: str):
        feed = self.fetcher.get_xml(country_name=country_name)
        entries = feed.findall("atom:entry", self.xml_namespace)
        return entries

    def _extract_entry(self, entry: xml.etree.ElementTree.Element):
        entry_fields = {}
        model_fields = list(MeteoalarmEntry.__fields__.keys())

        # handle geocode separately
        geocode_element = entry.find("./cap:geocode", namespaces=self.xml_namespace)
        entry_fields["cap__geocode"] = {
            f"{geocode_element.findtext('./atom:valueName', namespaces=self.xml_namespace)}": f"{geocode_element.findtext('./atom:value', namespaces=self.xml_namespace)}"  # noqa:E501
        }
        model_fields.remove("cap__geocode")

        for field in model_fields:
            key = field.replace("__", ":")
            e = entry.find(f"./{key}", namespaces=self.xml_namespace)
            if e is None:
                self.logger.warning(f"missing '{key}' field in entry")
                value = None
            elif len(list(e)) > 0:
                self.logger.warning(f"{e} is complex value")
                value = None
            else:
                value = e.text
            entry_fields[field] = value
        meteoalarm_entry = MeteoalarmEntry.parse_obj(entry_fields)
        return meteoalarm_entry

    def get_entries(self, country_name: str) -> List[MeteoalarmEntry]:
        entries = self.get_raw_entries(country_name)
        parsed_entries = list()
        for xml_entry in entries:
            meteo_entry = self._extract_entry(xml_entry)
            parsed_entries.append(meteo_entry)
        return parsed_entries

    def get_alerts(self, country_name: str) -> List[MeteoalarmEntry]:
        """Get all meteoalarm.org alerts for given :country_name"""
        entries_dict = [entry.dict(by_alias=True) for entry in self.get_entries(country_name)]
        return entries_dict
