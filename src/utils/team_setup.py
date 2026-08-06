import requests
from bs4 import BeautifulSoup
from src.parsers.team_parser import team_parser

def get_teams(division: str, year: int, competition: str) -> str:
    """takes as input division name, and year of the season returns a list of teams in this division"""
    url = (f"https://www.transfermarkt.de/{division}/startseite/wettbewerb/{competition}/plus/?saison_id={year}")
    print(f"{url}")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    return team_parser(soup)
