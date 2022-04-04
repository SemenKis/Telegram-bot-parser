from bs4 import BeautifulSoup
import requests

import os
import json
from abc import ABC
from abc import abstractmethod

"""Parser(url, path, accept, user_agent)"""
class Parser(ABC):

    @abstractmethod
    def _get_request(self) -> None:
        raise NotImplementedError


    @abstractmethod
    def _parse_data(self) -> None:
        raise NotImplementedError


    def _convert_to_json(self, path, obj):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4, ensure_ascii=False)
            if os.path.exists(path) == path:
                print(True)
