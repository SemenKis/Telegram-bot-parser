import requests
from bs4 import BeautifulSoup
from main_parse_class import Parser

class AhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0])
        response = src.text
        print(response)

    def _parse_data(self):
        pass

    def call(self):
        self._get_request()
        #self._parse_data()

def main():
    ahl_reg_season = AhlRegularSeasonParser('https://theahl.com/stats/standings')
    ahl_reg_season.call()