from .base_scraper import BaseScraper
from models.jobs import Job


class RemotarScraper(BaseScraper):

    def __init__(self, query):
        super().__init__(query)
        self.base_url = 'https://api.remotar.com.br/jobs?search='

    def build_url(self):
        formatted_query = self.query.lower()
        return f'{self.base_url}{formatted_query}'

    def parse(self, response):
        data = response.json()
        jobs = []

        for job in data['data']:
            job = Job(
                id=job['id'],
                title=job['title'],
                description=job['description'],
                url=f"https://remotar.com.br/job/{job['id']}",
                origin='REMOTAR'
            )
            jobs.append(job)

        return jobs