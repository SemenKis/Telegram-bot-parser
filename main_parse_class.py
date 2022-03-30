from bs4 import BeautifulSoup
import requests

import os
import json
from abc import ABC
from abc import abstractmethod

"""Parser(url, path, accept, user_agent)"""
class Parser(ABC):

    @abstractmethod
    def get_request(self) -> None:
        raise NotImplementedError


    @abstractmethod
    def parse_data(self) -> None:
        raise NotImplementedError


    def convert_to_json(self, path, obj):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4, ensure_ascii=False)
            if os.path.exists(path) == path:
                print(True)
