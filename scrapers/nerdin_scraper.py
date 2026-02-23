from bs4 import BeautifulSoup

from .base_scraper import BaseScraper
from models.jobs import Job


class NerdinScraper(BaseScraper):

    def __init__(self, query):
        super().__init__(query)
        self.base_url = "https://www.nerdin.com.br/vagas.php?busca="

    def build_url(self):
        formatted_query = self.query.replace(' ', '+').lower()
        return f'{self.base_url}{formatted_query}'

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []

        cards = soup.find_all("div", class_="vaga-card")

        for card in cards:
            job_title = card.find("h3", class_="vaga-titulo").get_text(strip=True)

            link_tag = card.find("a", class_="btn-ver-vaga")
            href = link_tag["href"]

            url_completa = "https://www.nerdin.com.br/" + href

            job_id = href.split("-")[-1].replace(".php", "")

            job = Job(
                id=job_id,
                title=job_title,
                description="",
                url=url_completa,
                origin='NERDIN'
            )

            jobs.append(job)

        return jobs