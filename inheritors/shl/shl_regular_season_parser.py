import json
from main_parse_class import Parser
import requests

class ShlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0])
        response = src.json()
        # print(response)
        with open('inheritors/shl/shl_regular_season_data.json', 'w', encoding='utf-8') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

    def _parse_data(self):
        with open('inheritors/shl/shl_regular_season_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            teams_info = []
            team_data = {}
            # team_data['records'] = []
            for item in data:
                team_data['records'] = []
                for team_info in item['stats']:
                    # print(team_info)
                    team_name = team_info['TeamCode']
                    team_standing = team_info['Rank']
                    gp = team_info['GP']
                    g = team_info['G']
                    ga = team_info['GA']
                    ot = team_info['OTL']
                    row = team_info['OTW']
                    pts = team_info['Points']

                    # print(team_standing, team_name, g, ga, ot, row, pts)

                    team_data['records'].append({
                        "team-position": team_standing,
                        "team-name": team_name,
                        "GP": gp,
                        "ROW": row,
                        "OT": ot,
                        "PTS": pts,
                    })
                # print(team_data)

                teams_info.append(team_data)
            with open('json_files/shl_regular_season_data.json', 'w', encoding='utf-8') as file:
                json.dump(teams_info, file, ensure_ascii=False, indent=4)

    def call(self):
        self._get_request()
        self._parse_data()

def main():
    url = 'https://www.shl.se/p/api/statistics/standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'

    shl_regular_season = ShlRegularSeasonParser(url)
    shl_regular_season.call()

