from main_parse_class import *

class ShlMatchesParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')
        date_container = soup.find_all(class_='rmss_c-schedule-game__date-container')
        matches_info = []
        for date_item in date_container:
            date = date_item.find(class_='rmss_t-styled__inner')
            print(f' --- {date.text} --- ')
            all_matches = date_item.find_all(class_='rmss_c-schedule-game__wrapper')
            for match in all_matches:
                team = match.find(class_='rmss_c-schedule-game__team is-home-team').find(class_='rmss_c-schedule-game__team-name')
                team_opposite = match.find(class_='rmss_c-schedule-game__team is-away-team').find(class_='rmss_c-schedule-game__team-name')
                team_results = match.find(class_='rmss_c-schedule-game__result is-gallery-layout').find('span', class_='rmss_c-schedule-game__team-result is-home-team')
                match_time = match.find(class_='rmss_c-schedule-game__start-time')
                str(team_results)
                if match_time == None:
                    print(f'{team.text} {team_opposite.text} | time not available')
                    continue
                else:
                    print(f'{team.text} {team_opposite.text} | {match_time.text}')
                matches_data = {
                    'Date and city': date.text,
                    'team': team.text,
                    'team_opposite': team_opposite.text,
                    'time': match_time.text,
                }
                matches_info.append(matches_data)
        print(matches_info)
        if len(matches_info) == 0:
            print('sorry, it is without information')
            return 0
        else:
            # super().convert_to_json('../json_files/shl_matches_data.json', matches_info)
            super().convert_to_json('json_files/shl_matches_data.json', matches_info)

accept = '*/*'
user_agent = 'mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'

def main():
    shl = ShlMatchesParser('https://www.shl.se/spelschema/SHL_2021_regular', 'html/shl_matches_info.html', accept=accept, user_agent=user_agent)
    shl.get_request()
    if shl.parse_data() == 0:
        return False




