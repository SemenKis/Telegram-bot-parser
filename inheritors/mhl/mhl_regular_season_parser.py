from main_parse_class import *

class MhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


    def _get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def _parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')
        conference_west = soup.find('div', class_='standing_item_title hidden-xs hidden-sm')
        conference_east = soup.find('div', class_='standing_item hidden-sm hidden-xs').find('div', class_='standing_item_title hidden-xs hidden-sm')
        teams_table_west = soup.find('table', class_='site_table site_table-blue').find_all('tr')
        teams_table_east = soup.find('table', class_='site_table site_table-red').find_all('tr')

        table_data = []
        team_data = {}
        team_data['conference'] = conference_west.text
        team_data['records'] = []
        for team_info in teams_table_west:
            team_standing = team_info.find(class_='standing_col_team_num')
            team_pict = team_info.find('img')
            team_name = team_info.find(class_='site_table_col_left').find('a')
            team_points = team_info.find_all('td')

            if None in [team_standing, team_pict, team_name]:
                continue

            team_data['records'].append({
                'logo': team_pict['src'],
                "team-position": team_standing.text,
                "team-name": team_name.text,
                "GP": team_points[3].text,
                "W": team_points[4].text,
                "ROW": team_points[5].text,
                "OT": team_points[7].text,
                "L": team_points[9].text,
                "GF": team_points[10].text,
                "PTS": team_points[11].text,
            })
        table_data.append(team_data)

        team_data_2 = {}
        team_data_2['conference'] = conference_east.text
        team_data_2['records'] = []
        for team_info in teams_table_east:
            team_standing = team_info.find(class_='standing_col_team_num')
            team_pict = team_info.find('img')
            team_name = team_info.find(class_='site_table_col_left').find('a')
            team_points = team_info.find_all('td')

            if None in [team_standing, team_pict, team_name]:
                continue

            team_data_2['records'].append({
                'logo': team_pict['src'],
                "team-position": team_standing.text,
                "team-name": team_name.text,
                "GP": team_points[3].text,
                "W": team_points[4].text,
                "ROW": team_points[5].text,
                "OT": team_points[7].text,
                "L": team_points[9].text,
                "GF": team_points[10].text,
                "PTS": team_points[11].text,
            })
        table_data.append(team_data_2)

        # super().convert_to_json('../../json_files/mhl_regular_season_data.json', table_data)
        super()._convert_to_json('json_files/mhl_regular_season_data.json', table_data)

    def call(self):
        self._get_request()
        self._parse_data()

accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'

def main():
    mhl_regular_season = MhlRegularSeasonParser('https://mhl.khl.ru/standings/regular/', accept=accept, user_agent=user_agent)
    mhl_regular_season.call()





