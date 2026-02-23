from scrapers.remotar_scraper import RemotarScraper
from scrapers.nerdin_scraper import NerdinScraper
from scrapers.trabalhabr_scraper import TrabalhaBrScraper
from database.db import JobRepository
from reports.report_service import ReportService


def main():
    query = ['estagio ti']

    for q in query:
        if not q:
            print('Busca inválida')
            return

        all_jobs = []

        scrapers = [
            RemotarScraper(q),
            NerdinScraper(q),
            TrabalhaBrScraper(q)
        ]
        
        db = JobRepository()

        counter = 0
        for scraper in scrapers:
            jobs = scraper.run()

            for job in jobs:
                db.save_job(job)
                all_jobs.append(job)
                counter += 1

        ReportService.export_to_excel(query=q, jobs=all_jobs)

        db.delete_old_jobs()
        print('\nBusca Realizada!')
        print(f'{counter} resultado{'s' if counter > 1 else ''} encontrado{'s' if counter > 1 else ''} para "{q.capitalize()}" \n')

if __name__ == "__main__":
    main()
