from abc import ABC, abstractmethod

import requests


class BaseScraper(ABC):

    def __init__(self, query):
        self.query = query

    @abstractmethod
    def build_url(self):
        pass

    def get(self):
        url = self.build_url()
        response = requests.get(url)
        response.raise_for_status()
        return response
    
    @abstractmethod
    def parse(self, response):
        pass

    def run(self):
        response = self.get()
        return self.parse(response=response)