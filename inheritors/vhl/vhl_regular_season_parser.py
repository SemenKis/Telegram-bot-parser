import requests
from main_parse_class import Parser
# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class VhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        # req = Request(self.args[0])
        # self.webpage = urlopen(req).read()
        src = requests.get(self.args[0])
        self.response = src.text

    def _parse_data(self):
        soup = BeautifulSoup(self.response, 'lxml')
        wrapper = soup.find(class_='sp-CenterWrapper')
        table_container = wrapper.find(class_='sp-Table-container')
        table = table_container.find(class_='sp-Table-tbody')

        teams_info = []
        team_data = {}
        team_data['records'] = []

        for team_info in table:
            team_standing = team_info.find(class_='sp-Table-cell').text
            team_name = team_info.find(class_='sp-ImageWithName__name').text
            team_logo = team_info.find(class_='sp-ImageWithName__image').find('img')
            score = team_info.find_all(class_='sp-Table-cell')

            gp = score[2].text
            w = score[3].text
            row = score[4].text
            l = score[5].text
            otl = score[6].text
            gf = score[7].text
            pts = score[8].text

            team_data['records'].append({
                "logo": f"https:{team_logo['src']}",
                "team-position": team_standing,
                "team-name": team_name,
                "GP": gp,
                "W": w,
                "ROW": row,
                "OT": otl,
                "L": l,
                "GF": gf,
                "PTS": pts
            })
        teams_info.append(team_data)
        # super()._convert_to_json('../../json_files/vhl_regular_season_data.json', teams_info)
        super()._convert_to_json('json_files/vhl_regular_season_data.json', teams_info)


    def call(self):
        self._get_request()
        self._parse_data()


url = 'https://www.sport-express.ru/hockey/L/vhl/2021-2022/'

def main():
    vhl_regular_season = VhlRegularSeasonParser(url)
    vhl_regular_season.call()
