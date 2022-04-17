from main_parse_class import *


class MhlParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def _parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')

        calendar_items = soup.find('div', class_='b_calendar_items_group active')
        calendar_item = calendar_items.find_all(class_='calendar_dayitems')
        # print(calendar_item)
        matches_info = []
        for item in calendar_item:

            match = {}

            date = item.find(class_='b_calendar_items_day_date ib')
            teams = item.find(class_='row').find_all(class_='col-xs-12 col-lg-6')
            match['date'] = date.text
            match['records'] = []
            for team_cont in teams:
                team = team_cont.find(class_='b_calendar_item_col b_calendar_item_col-left').find(class_='b_calendar_item_team_name')
                # team_logo = team_cont.find(class_='b_calendar_item_col b_calendar_item_col-left').find(class_='b_calendar_item_team_logo').find('img')
                match_date = team_cont.find(class_='b_calendar_item_game_date')
                match_time = team_cont.find(class_='b_calendar_item_game_time')
                team_opposite = team_cont.find(class_='b_calendar_item_col b_calendar_item_col-right').find(class_='b_calendar_item_team_name')
                team_opposite_logo = team_cont.find(class_='b_calendar_item_col b_calendar_item_col-right').find(class_='b_calendar_item_team_logo').find('img')

                match['records'].append(
                    {
                        "Date and city": match_date.text,
                        "team": team.text,
                        "team-opposite": team_opposite.text,
                        "time": match_time.text
                    }
                )

            matches_info.append(match)

        # super()._convert_to_json('../../json_files/mhl_playoffs_data.json', matches_info) # если файл вызывается из вне
        super()._convert_to_json('json_files/mhl_playoffs_data.json', matches_info)

    def call(self):
        self._get_request()
        self._parse_data()


def main():
    parser = MhlParser('https://mhl.khl.ru/calendar/', accept='*/*', user_agent=
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
    parser.call()

main()







