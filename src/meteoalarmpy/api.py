import requests

from .fetcher import Fetcher


class MeteoAlarm:
    def __init__(self):
        self.fetcher = Fetcher()

    def get_entries(self, country_name: str):
        ns = {'atom': 'http://www.w3.org/2005/Atom',
              'cap': 'urn:oasis:names:tc:emergency:cap:1.2'}
        feed = self.fetcher.get_xml(country_name=country_name)
        entries = feed.findall('atom:entry', ns)
        return entries
