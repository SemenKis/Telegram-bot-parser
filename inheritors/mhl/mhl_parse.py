from main_parse_class import *


class MhlParser(Parser):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.args = args
        self.kwargs = kwargs

    def parse_data(self):
        super().parse_data()
        matches_blocks = self.soup.find(class_='b_calendar_items_group active').find_all(class_='calendar_dayitems')
        # print(matches_blocks)
        list_of_matches = []
        for block in matches_blocks:
           # print(block)
            date = block.find(class_='b_calendar_items_day_date ib')
            match = block.find(class_='row').find_all(class_='col-xs-12')
            # print(match_info)
            for item in match:
                # print(item)
                team = item.find(class_='b_calendar_item_col b_calendar_item_col-40 b_calendar_item_col-left').find(class_='b_calendar_item_team_name')
                team_opposite = item.find(class_='b_calendar_item_col b_calendar_item_col-right b_calendar_item_col-40 align-right').find(class_='b_calendar_item_team_name')
                print(team.text ,team_opposite.text, date.text)

                match_info = {
                    'Date and city': date.text,
                    'team': team.text,
                    'team_opposite': team_opposite.text,
                    'time': ''
                }

                list_of_matches.append(match_info)

        # print(list_of_matches)
        # super().convert_to_json('../../json_files/mhl_playoffs_data.json', list_of_matches) # если файл вызывается из вне
        super().convert_to_json('json_files/mhl_playoffs_data.json', list_of_matches)



# parser = MhlParser('https://mhl.khl.ru/calendar/', '../html/mhl_calendar.html', accept='*/*', user_agent=
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
# parser.get_request()
# parser.parse_data()

def main():
    parser = MhlParser('https://mhl.khl.ru/calendar/', accept='*/*', user_agent=
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
    parser.get_request()
    parser.parse_data()

    print(__name__)


