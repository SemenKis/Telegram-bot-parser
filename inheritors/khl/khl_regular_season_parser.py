
from main_parse_class import Parser

class KhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def parse_data(self):
        super().parse_data()
        tables = self.soup.find_all(class_='k-data_table')
        west_table = tables[0].find_all('tr')
        table_name = self.soup.find_all(class_='m-fl')
        # print(table_name)
        east_table = tables[1].find_all('tr')
        table_data = []
        for team_info in west_table:
            info = team_info.find_all('td')
            if len(info) == 0:
                continue
            team_standing = info[0].text.strip()
            team_name = info[1].text.strip()
            games = info[2].text.strip()
            wins = info[3].text.strip()
            ot_wins = info[4].text.strip()
            ot_losses = info[7].text.strip()
            losses = info[8].text.strip()
            gf = info[9].text.strip()
            pts = info[10].text.strip()
            team_data = {
                'conference': table_name[0].text,
                "team-position": team_standing,
                "team-name": team_name,
                "GP": games,
                "W": wins,
                "ROW": ot_wins,
                "OT": ot_losses,
                "L": losses,
                "GF": gf,
                "PTS": pts
            }
            table_data.append(team_data)
        for team_info in east_table:
            info = team_info.find_all('td')
            if len(info) == 0:
                continue
            team_standing = info[0].text.strip()
            team_name = info[1].text.strip()
            games = info[2].text.strip()
            wins = info[3].text.strip()
            ot_wins = info[4].text.strip()
            ot_losses = info[7].text.strip()
            losses = info[8].text.strip()
            gf = info[9].text.strip()
            pts = info[10].text.strip()
            team_data = {
                'conference': table_name[1].text,
                "team-position": team_standing,
                "team-name": team_name,
                "GP": games,
                "W": wins,
                "ROW": ot_wins,
                "OT": ot_losses,
                "L": losses,
                "GF": gf,
                "PTS": pts
            }
            table_data.append(team_data)
        # super().convert_to_json('../../json_files/khl_regular_season_data.json', table_data)
        super().convert_to_json('json_files/khl_regular_season_data.json', table_data)
        print(table_data)


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'

# khl_regular_season = KhlRegularSeasonParser('https://www.khl.ru/standings/1097/conference/', accept='*/*', user_agent=user_agent )
# khl_regular_season.get_request()
# khl_regular_season.parse_data()

def main():
    khl_regular_season = KhlRegularSeasonParser('https://www.khl.ru/standings/1097/conference/', accept='*/*', user_agent=user_agent )
    khl_regular_season.get_request()
    khl_regular_season.parse_data()