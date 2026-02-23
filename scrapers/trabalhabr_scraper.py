import requests
from bs4 import BeautifulSoup

from .base_scraper import BaseScraper
from models.jobs import Job


class TrabalhaBrScraper(BaseScraper):
    # Model define a modalidade do trabalho (Presencial, Híbrido e Remoto) - EM IMPLEMENTAÇÃO

    def __init__(self, query, model=None):
        super().__init__(query)
        self.base_url = 'https://www.trabalhabrasil.com.br/'
        self.model = '' if model is None else model
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def build_url(self):
        formatted_query = self.query.replace(' ', '-')
        search_url = f'vagas-de-emprego/{formatted_query}?modalidade={self.model}'
        return f'{self.base_url}{search_url}'

    def get(self):
        url = self.build_url()
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = []

        cards = soup.find_all('a', class_='job-link')

        for card in cards:

            title = card.find('h2', class_='job-title').get_text(strip=True)
            href = card['href'][1:]
            job_id = ''.join(c for c in href if c.isdigit())
            url = f'{self.base_url}{href}'

            job = Job(
                id=job_id,
                title=title,
                description='',
                url=url,
                origin='TRABALHA_BR'
            )

            jobs.append(job)
        
        return jobs