from .fetcher import Fetcher


class MeteoAlarm:
    def __init__(self):
        self.fetcher = Fetcher()
        self.xml_namespace = {
            "atom": "http://www.w3.org/2005/Atom",
            "cap": "urn:oasis:names:tc:emergency:cap:1.2",
        }

    def get_entries(self, country_name: str):
        feed = self.fetcher.get_xml(country_name=country_name)
        entries = feed.findall("atom:entry", self.xml_namespace)
        return entries

    def get_parsed_entries(self, country_name: str):
        entries = self.get_entries(country_name)
        parsed_entries = list()
        for entry in entries:
            p_entry = {
                x.tag: x.text for x in entry.findall("./cap:*", self.xml_namespace)
            }
            parsed_entries.append(p_entry)
        return parsed_entries
