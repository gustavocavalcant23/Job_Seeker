import sqlite3
from datetime import datetime, timedelta


class JobRepository:

    def __init__(self, db_name='jobs.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT,
                title TEXT,
                description TEXT,
                url TEXT,
                origin TEXT,
                created_at TEXT,
                UNIQUE(id, origin)
            )
        """)
        self.conn.commit()

    def save_job(self, job):
        try:
            self.conn.execute("""
                INSERT INTO jobs (id, title, description, url, origin, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                job.id,
                job.title,
                job.description,
                job.url,
                job.origin,
                job.created_at.isoformat()
            ))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def delete_old_jobs(self, days=30):
        limite = datetime.now() - timedelta(days=days)

        self.conn.execute("""
            DELETE FROM jobs
            WHERE created_at < ?
        """, (limite.isoformat(),))

        self.conn.commit()