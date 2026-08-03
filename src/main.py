import requests
import pandas as pd

from models.team import Team
from bs4 import BeautifulSoup
from parsers.team_parser import team_parser
from parsers.market_value_parser import MarketValueParser
from parsers.player_parser import PlayerParser
from scrapers.scrape_teams import scrape_teams
from transform.clean_data import clean_data

def main(): 
    # setup for team parser
    division = 'bundesliga'
    year = 2026
    # How to manipulate strings in python, maybe make a prompt for year and divison 

    url = ("https://www.transfermarkt.de/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2026")

    print(f"loading {division}-teams of season {year}")
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # Parse all teams from the league page 
    teams = team_parser(soup)
    print(f"Found {len(teams)} teams")

    #  Configure which parsers should run for each team
    parsers = (
        PlayerParser(),
        MarketValueParser(),
    )
    # Scrape every team
    raw_data = scrape_teams(
        teams=teams,
        parsers=parsers,
        year=year,
    )

    # raw_data = pd.read_csv("players_transfermarkt.csv")
    data = clean_data(raw_data)
    print(data.head())
    # print(raw_data.shape)

    data.to_csv(
        "players_transfermarkt.csv",
        index=False
    )

if __name__=="__main__":
    main()