from main_parse_class import *

class KhlMatchesParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        self.src = response.text

    def _parse_data(self):
        soup = BeautifulSoup(self.src, 'lxml')
        all_slider_items = soup.find_all('table', class_='b-matches_data m-w_100')

        match_info = []
        for match in all_slider_items:
            match_data = {}

            date = match.find(class_='e-matches_data_center')
            match_data['date'] = date.text.strip()
            match_data['records'] = []

            team = match.find(class_='b-matches_data_middle').find(class_='e-matches_data_left')
            team_opposite = match.find(class_='b-matches_data_middle').find(class_='e-matches_data_right')
            time = match.find(class_='b-matches_data_bottom').find(class_='e-matches_data_left').find(class_='e-cut')
            if time == None:
                continue
            else:
                #print(team.text, team_opposite.text," | " ,date.text," | " ,time.text)
                match_data['records'].append({
                    'team': team.text,
                    'team-opposite': team_opposite.text,
                    'time': time.text[0:5]
                })
                match_info.append(match_data)
        # super()._convert_to_json('../../json_files/khl_playoffs_data.json', match_info)
        super()._convert_to_json('json_files/khl_playoffs_data.json', match_info)


    def call(self):
        self._get_request()
        self._parse_data()

def main():
    khl = KhlMatchesParser('https://www.khl.ru/', accept='*/*',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
    khl.call()



