import xml.etree.ElementTree as ET

from requests import Session


class Fetcher:
    URL_ATOM_XML_TEMPLATE = (
        "https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-{0}"
    )
    NAMESPACES = {
        "atom": "http://www.w3.org/2005/Atom",
        "cap": "urn:oasis:names:tc:emergency:cap:1.2",
    }

    def __init__(self):
        self._session = Session()

    def _get_raw_xml(self, country_name: str):
        result = self._session.get(
            url=self.URL_ATOM_XML_TEMPLATE.format(country_name.lower())
        )
        result.raise_for_status()
        return result.text

    def get_xml(self, country_name: str) -> ET.Element:
        r_xml = self._get_raw_xml(country_name=country_name)
        for k, v in self.NAMESPACES.items():
            ET.register_namespace(k, v)
        xml_root = ET.fromstring(r_xml)
        return xml_root
