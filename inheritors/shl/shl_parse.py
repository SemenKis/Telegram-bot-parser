from main_parse_class import *

class ShlMatchesParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0], headers=self.kwargs)
        self.response = src.text


    def _parse_data(self):
        soup = BeautifulSoup(self.response, 'lxml')

        match_table = soup.find_all(class_='rmss_c-schedule-game__date-container')
        

    def call(self):
        self._get_request()
        self._parse_data()

shl_playoffs = ShlMatchesParser('https://www.shl.se/spelschema/SHL_2021_playoff')
shl_playoffs.call()




