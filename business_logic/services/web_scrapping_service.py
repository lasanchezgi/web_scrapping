import requests
from bs4 import BeautifulSoup

class WebScrappingService:
    web_url: str
    attribute: str

    def __init__ (self, web_url: str, attribute: str = 'text'):
        self.web_url = web_url
        self.attribute = attribute
    
    def get_text(self):
        response = requests.get(self.web_url)
        response.raise_for_status()

        scrap_obj = BeautifulSoup(response.text, 'html.parser')
        return scrap_obj.get_text()