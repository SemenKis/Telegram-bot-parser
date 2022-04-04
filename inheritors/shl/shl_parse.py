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
        match_data = {}
        for match in match_table:
            # print(match)
            match_date = match.find(class_='rmss_t-styled__inner')
            teams_info = match.find(class_='rmss_c-schedule-game__date-games')
            match_data['Date and City'] = match_date.text
            for teams in teams_info:
                # print(teams)
                teams_block_first = teams.find(class_='rmss_c-schedule-game__row-wrapper is-visible is-first')
                teams_block_last = teams.find(class_='rmss_c-schedule-game__row-wrapper is-visible is-last')
                print(teams_block_first)
                print(teams_block_last)

    def call(self):
        self._get_request()
        self._parse_data()

shl_playoffs = ShlMatchesParser('https://www.shl.se/spelschema/SHL_2021_playoff')
shl_playoffs.call()




