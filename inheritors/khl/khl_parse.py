from main_parse_class import *

class KhlMatchesParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')
        all_slider_items = soup.find('div', class_="b-feed_matches m-slick_slider").find_all('table', class_='b-matches_data m-w_100')
        matches_data = []
        for slider_item in all_slider_items:
            match_date_and_city = slider_item.find(class_='e-matches_data_center')
            match_time = slider_item.find(class_='b-matches_data_bottom').find(class_='e-cut')
            match_teams = slider_item.find(class_='b-matches_data_middle')
            match_team = match_teams.find(class_='e-matches_data_left')
            match_team_opposite = match_teams.find(class_='e-matches_data_right')

            if match_time == None:
                continue
            else:
                matches_data.append({
                    'Date and city': match_date_and_city.text.strip() + ', ' + match_time.text[11:],
                    'team': match_team.text,
                    'team_opposite': match_team_opposite.text,
                    'time': match_time.text[:5]
                })
        # super().convert_to_json('../../json_files/khl_matches_data.json', matches_data)
        super().convert_to_json('json_files/khl_matches_data.json', matches_data)


def main():
    khl = KhlMatchesParser('https://www.khl.ru/', accept='*/*',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
    khl.get_request()
    khl.parse_data()


