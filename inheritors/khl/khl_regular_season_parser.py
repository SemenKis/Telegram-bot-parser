from main_parse_class import *


class KhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def _parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')
        tables = soup.find(class_='m-top_panel').find_all(class_='b-data_row')[0:2]
        tables_data = []
        for table in tables:
            conference = table.find(class_='b-subtitle_nav_cover m-clear').find(class_='m-fl')

            teams_info = {}
            teams_info['conference'] = conference.text
            teams_info['records'] = []

            table_info = table.find('table').find_all('tr')

            for info in table_info:
                team_info = info.find_all('td')
                if len(team_info) == 0:
                    continue
                team_position = team_info[0].text
                team_logo = team_info[1].find('img')
                team_name = team_info[1].text.strip()
                gp = team_info[2].text
                wins = team_info[3].text
                ot_wins = team_info[4].text
                ot_losses = team_info[7].text
                losses = team_info[8].text
                gf = team_info[9].text
                pts = team_info[10].text

                teams_info['records'].append({
                    "logo": f"https://www.khl.ru{team_logo['src']}",
                    "team-position": team_position,
                    "team-name": team_name,
                    "GP": gp,
                    "W": wins,
                    "ROW": ot_wins,
                    "OT": ot_losses,
                    "L": losses,
                    "GF": gf,
                    "PTS": pts
                })
            tables_data.append(teams_info)
        # super()._convert_to_json('../../json_files/khl_regular_season_data.json', tables_data)
        super()._convert_to_json('json_files/khl_regular_season_data.json', tables_data)

    def call(self):
        self._get_request()
        self._parse_data()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'

def main():
    khl_regular_season = KhlRegularSeasonParser('https://www.khl.ru/standings/1097/conference/', accept='*/*', user_agent=user_agent )
    khl_regular_season.call()
