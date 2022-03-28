from bs4 import BeautifulSoup
import requests
# import lxml
import os
import json
# from abc import ABC
from abc import abstractmethod

"""Parser(url, path, accept, user_agent)"""
class Parser():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.soup = ''
        self.src = ''

    def get_request(self):
        response = requests.get(self.args[0], headers=self.kwargs)
        # print(response.text)
        self.src = response.text


    @abstractmethod
    def parse_data(self):
        html = self.src
        self.soup = BeautifulSoup(html, 'lxml')

    @abstractmethod
    def convert_to_json(self, path, obj):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4, ensure_ascii=False)
            if os.path.exists(path) == path:
                print(True)
