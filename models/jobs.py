from datetime import datetime


class Job:

    def __init__(self, id, title, description, url, origin):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.origin = origin
        self.created_at = datetime.now()

    def unique_keys(self):
        return f"{self.origin}_{self.id}"

    def __repr__(self):
        return f"< Job {self.id} - {self.title} >"