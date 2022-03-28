from main_parse_class import Parser

class MhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    def parse_data(self):
        super().parse_data()

        # teams_table = self.soup.find('table', class_='site_table site_table-blue').find_all('tr')
        conference_west = self.soup.find('div', class_='standing_item_title hidden-xs hidden-sm')
        conference_east = self.soup.find('div', class_='standing_item hidden-sm hidden-xs').find('div', class_='standing_item_title hidden-xs hidden-sm')
        teams_table_west = self.soup.find('table', class_='site_table site_table-blue').find_all('tr')
        teams_table_east = self.soup.find('table', class_='site_table site_table-red').find_all('tr')

        table_data = []
        for team_info in teams_table_west:
            # print(team_info)
            team_standing = team_info.find(class_='standing_col_team_num')
            team_pict = team_info.find(class_='standing_col_team_logo')
            team_name = team_info.find(class_='site_table_col_left').find('a')
            team_points = team_info.find_all('td')
            # тут вопрос
            if team_standing == None:
                continue
            # print(team_standing.text.strip(), team_name.text.strip())
            # print(team_points)
            # print(f'количество проведенных игр: {team_points[3].text}')
            # print(f'выигрыши: {team_points[4].text}')
            # print(f'выигрыши в овертайме: {team_points[5].text}')
            # print(f'выигрыши в послематчевых буллитах: {team_points[6].text}')
            # print(f'проигрыши в послематчевых буллитах: {team_points[7].text}')
            # print(f'проигрыши в овертайме: {team_points[8].text}')
            # print(f'проигрыши: {team_points[9].text}')
            # print(f'заброшенные шайбы: {team_points[10].text}')
            # print(f'очки: {team_points[11].text}')
            # print(' ')

            team_data = {
                'conference': conference_west.text,
                "team-position": team_standing.text,
                "team-name": team_name.text,
                "GP": team_points[3].text,
                "W": team_points[4].text,
                "ROW": team_points[5].text,
                "OT": team_points[7].text,
                "L": team_points[9].text,
                "GF": team_points[10].text,
                "PTS": team_points[11].text,
            }
            table_data.append(team_data)

        for team_info in teams_table_east:
            team_standing = team_info.find(class_='standing_col_team_num')
            team_pict = team_info.find(class_='standing_col_team_logo')
            team_name = team_info.find(class_='site_table_col_left').find('a')
            team_points = team_info.find_all('td')
            # тут вопрос
            if team_standing == None:
                continue
            # print(team_standing.text.strip(), team_name.text.strip())
            # print(f'количество проведенных игр: {team_points[3].text}')
            # print(f'выигрыши: {team_points[4].text}')
            # print(f'выигрыши в овертайме: {team_points[5].text}')
            # print(f'выигрыши в послематчевых буллитах: {team_points[6].text}')
            # print(f'проигрыши в послематчевых буллитах: {team_points[7].text}')
            # print(f'проигрыши в овертайме: {team_points[8].text}')
            # print(f'проигрыши: {team_points[9].text}')
            # print(f'заброшенные шайбы: {team_points[10].text}')
            # print(f'очки: {team_points[11].text}')
            # print(' ')

            team_data = {
                'conference': conference_east.text,
                "team-position": team_standing.text,
                "team-name": team_name.text,
                "GP": team_points[3].text,
                "W": team_points[4].text,
                "ROW": team_points[5].text,
                "OT": team_points[7].text,
                "L": team_points[9].text,
                "GF": team_points[10].text,
                "PTS": team_points[11].text,
            }
            table_data.append(team_data)

        print(table_data)
        # super().convert_to_json('../../json_files/mhl_regular_season_data.json', table_data)
        super().convert_to_json('json_files/mhl_regular_season_data.json', table_data)





accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'


# mhl_regular_season = MhlRegularSeasonParser('https://mhl.khl.ru/standings/regular/', accept=accept, user_agent=user_agent)
# mhl_regular_season.get_request()
# mhl_regular_season.parse_data()

def main():
    mhl_regular_season = MhlRegularSeasonParser('https://mhl.khl.ru/standings/regular/', accept=accept, user_agent=user_agent)
    mhl_regular_season.get_request()
    mhl_regular_season.parse_data()
