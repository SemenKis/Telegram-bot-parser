from main_parse_class import Parser
from urllib.request import Request, urlopen
# import requests
from bs4 import BeautifulSoup

class VhlMatchesParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        req = Request(self.args[0], headers=self.args[1])
        self.webpage = urlopen(req).read()


    def _parse_data(self):
        soup = BeautifulSoup(self.webpage, 'lxml')
        playoffs = soup.find(class_='inner-tabs__content show')
        playoffs_table = playoffs.find('table')
        teams = playoffs_table.find_all('tr')

        teams_info = []
        teams_data = {}
        teams_data['group_1'] = []
        teams_data['group_2'] = []

        count = 0
        for team_info in teams:
            team = team_info.find_all('td', class_='table__cell')
            # print(team)
            if len(team) == 0:
                continue
            team_name = team[0].text.strip()
            game_1 = team[1].text.strip()
            game_2 = team[2].text.strip()
            game_3 = team[3].text.strip()
            game_4 = team[4].text.strip()
            game_5 = team[5].text.strip()
            game_6 = team[6].text.strip()
            game_7 = team[7].text.strip()

            count += 1
            if count % 2 == 0:
                teams_data[f'group_1'].append(
                    {
                    "team-name": team_name,
                    "first-game": game_1,
                    "second-game": game_2,
                    "third-game": game_3,
                    "fourth-game": game_4,
                    "fifth-game": game_5,
                    "sixth-game": game_6,
                    "seventh-game": game_7
                    }
                )
            else:
                teams_data[f'group_2'].append(
                    {
                        "team-name": team_name,
                        "first-game": game_1,
                        "second-game": game_2,
                        "third-game": game_3,
                        "fourth-game": game_4,
                        "fifth-game": game_5,
                        "sixth-game": game_6,
                        "seventh-game": game_7
                    }
                )

        teams_info.append(teams_data)

        # super()._convert_to_json('../../json_files/vhl_playoffs_data.json', teams_info)
        super()._convert_to_json('json_files/vhl_playoffs_data.json', teams_info)


    def call(self):
        self._get_request()
        self._parse_data()

header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}


accept = '*/*'
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'

def main():
    vhl = VhlMatchesParser('https://www.vhlru.ru/standings/playoff/1104/15020/', header)
    vhl.call()


