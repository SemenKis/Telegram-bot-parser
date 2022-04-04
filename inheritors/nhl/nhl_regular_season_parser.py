
from main_parse_class import *
import json

class NhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0], headers=self.kwargs)
        response = src.json()
        with open('inheritors/nhl/nhl_regular_season.json', 'w', encoding='utf-8') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

    def _parse_data(self):
        with open('inheritors/nhl/nhl_regular_season.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            records = data['records']
            self.teams_info = []

            for item in records:
                division = item['division']['name']
                conference = item['conference']['name']
                team = item['teamRecords']

                team_data = {}

                team_data['conference'] = conference
                team_data['division'] = division
                team_data['records'] = []
                for info in team:
                    team_standing = info['divisionRank']
                    team_name = info['team']['name']
                    gp = info['gamesPlayed']
                    w = info['leagueRecord']['wins']
                    l = info['leagueRecord']['losses']
                    ot = info['leagueRecord']['ot']
                    pts = info['points']
                    row = info['row']
                    gf = info['goalsScored']
                    ga = info['goalsAgainst']

                    team_data['records'].append({
                        "team-position": team_standing,
                        "team-name": team_name,
                        "GP": gp,
                        "W": w,
                        "ROW": row,
                        "OT": ot,
                        "L": l,
                        "GF": gf,
                        "PTS": pts,
                    })

                self.teams_info.append(team_data)

            # super().convert_to_json('../../json_files/nhl_regular_season_data.json', self.teams_info)
            super()._convert_to_json('json_files/nhl_regular_season_data.json', self.teams_info)

    def call(self):
        self._get_request()
        self._parse_data()

accept = '*/*'
user_agent = 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'

def main():
    nhl_regular_season = NhlRegularSeasonParser('https://statsapi.web.nhl.com/api/v1/standings', accept=accept,user_agent=user_agent)
    nhl_regular_season.call()

