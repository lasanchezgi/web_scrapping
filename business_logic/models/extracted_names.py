from uuid import UUID
from datetime import datetime
from utils.check_formats import is_web_url

class ExtractedNames:
    id: UUID | None
    website: str
    date: datetime | None
    name: list

    def __init__(self, website: str, names: list[str]):
        self.website = website
        self.names = names
    
    def validate(self):
        if not is_web_url(self.website):
            return False