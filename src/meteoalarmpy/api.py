import logging
import xml.etree.ElementTree
from typing import Dict, List

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

    def get_alerts(self, country_name: str, province_name: str) -> List[Dict]:
        """Get all meteoalarm.org alerts for given :country_name and :province_name"""
        entries = self.get_entries(country_name)  # type:List[MeteoalarmEntry]
        # the emma_id will be better, but we don't have any source implemented yet
        # meteoalarm.org provides list of geocodes, but it's heavy (tens of megabytes uncompressed)
        province_entries = [
            entry
            for entry in entries
            if str(entry.cap__areaDesc).lower() == province_name.lower()
        ]
        entries_dict = [entry.dict(by_alias=True) for entry in province_entries]
        return entries_dict
