import requests

from models.team import Team
from bs4 import BeautifulSoup
from parsers.team_parser import team_parser
from parsers.market_value_parser import MarketValueParser
from parsers.player_parser import PlayerParser
from scrapers.scrape_teams import scrape_teams


def main(): 
    # setup for team parser
    division = 'bundesliga'
    year = 2026
    # How to manipulate strings in python, maybe make a prompt for year and divison 

    url = ("https://www.transfermarkt.de/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2026")
    print(url)
    headers = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0"}

    print(f"loading {division}-teams of season {year}")
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # Parse all teams from the league page 
    teams = team_parser(soup)
    print(f"Found {len(teams)} teams")

     # Configure which parsers should run for each team
    parsers = (
        PlayerParser(),
        MarketValueParser(),
    )

    # Scrape every team
    data = scrape_teams(
        teams=teams,
        parsers=parsers,
        year=year,
    )

    print(data.head())
    print(data.shape)

    data.to_csv(
        "players_transfermarkt.csv",
        index=False
    )

if __name__=="__main__":
    main()