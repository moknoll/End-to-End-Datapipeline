from src.scrapers.tm_scraper import TmScraper
from src.models.team import Team
from collections.abc import Sequence
from src.parsers.base_parser import Parser
import pandas as pd

def scrape_teams(teams: list[Team], parsers: Sequence[Parser], year: int) -> pd.DataFrame: 
    dataframes = []

    for team in teams: 
        scraper = TmScraper(team=team, parsers=parsers, year=year)
        dataframes.append(scraper.run())
    
    return pd.concat(dataframes, ignore_index=True)
