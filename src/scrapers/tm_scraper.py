from bs4 import BeautifulSoup
from dataclasses import dataclass
from models.team import Team
from parsers.parser import Parser
from collections.abc import Sequence
import pandas as pd
import httpx 

@dataclass
class TmScraper: 
    """Scrape data form transfermarkt for a given team and year"""
    team: Team
    parsers: Sequence[Parser]
    year: int 
    url: str = (
        "https://www.transfermarkt.de/{name}/kader/verein/{id}}/saison_id/{year}]/plus/1"
        )

    def run(self) -> pd.DataFrame: 
        """Run scraping proces"""
        url = self.url.format(name=self.team.name, id=self.team.id, year=self.year)
        print(f"Scraping: {self.team.name} - {self.year}")
        soup = self._get_soup_content(url)
        data = pd.concat(
            [parser.parse(soup) for parser in self.parser], axis=1)
        data["season"] = self.year #add season to dataframe
        data["team"] = self.team.name # add team name to dataframe
        return data

    def _get_soup_content(self, url: str) -> BeautifulSoup: 
        """Get the html contetn from a given TM url"""
        resp = self._make_request(url)
        return BeautifulSoup(resp.content, "html.parser")
    
    def _make_request(self, url: str) -> httpx.Response: 
        """Make a request to a given TM url"""
        try: 
            response = httpx.get(url, headers={
                "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0"
            }, timeout=60)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e: 
            print(f"HTTP error occured: {e}")
            raise e
        

