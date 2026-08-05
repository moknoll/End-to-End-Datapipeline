import os

from parsers.market_value_parser import MarketValueParser
from parsers.player_parser import PlayerParser
from scrapers.scrape_teams import scrape_teams
from transform.clean_data import clean_data
from loaders.db_loader import PostgresLoader
from utils.logger import logger
from utils.team_setup import get_teams 

def main(): 
    logger.info("Starting ETL pipeline")
    year=2026
    division="bundesliga"
    csv=True

    # Extract
    teams = get_teams(division, year)
    raw_data = scrape_teams(teams=teams,parsers=(PlayerParser(), MarketValueParser()),year=year)

    # Transform
    data = clean_data(raw_data)

    # Load
    loader = PostgresLoader(os.getenv("DATABASE_URL"))
    loader.load_teams(teams)
    team_mapping = loader.get_team_mapping()
    data["team_id"] = data["team"].map(team_mapping)
    data.drop(columns=["team"], inplace=True)
    loader.load_players(data)
    if csv == True: 
        data.to_csv("../data/tm_stats_{division}_{year}.csv")
        logger.info("CSV file stored to root.")
    logger.info("ETL pipeline finished successfully.")

if __name__=="__main__":
    main()