from src.models.team import Team
from bs4 import BeautifulSoup

def team_parser(soup: BeautifulSoup) -> list[Team]:
    team_info = soup.find_all("td", {"class": "hauptlink no-border-links"})
    teams = []

    for team in team_info:
        link = team.find("a")
        if not link:
            continue
        parts = link["href"].split("/")
        teams.append(Team(name=parts[1], id=parts[4]))    
    return teams