import pandas as pd

from src.parsers.market_value_parser import MarketValueParser
from src.parsers.player_parser import PlayerParser
from src.scrapers.scrape_teams import scrape_teams
from src.transform.clean_data import clean_data
from src.loaders.load_data_in_db import load_db
from src.utils.logger import logger
from src.utils.team_setup import get_teams 

def main(): 
    logger.info("Starting ETL pipeline")
    year=2026
    division="bundesliga"
    competition="L1"
    csv=True

    # Extract
    teams = get_teams(division, year, competition)
    raw_data = scrape_teams(teams=teams,parsers=(PlayerParser(), MarketValueParser()),year=year)
    logger.info("All Teams Data scraped...starting data cleaning now.")

    # Transform
    data = clean_data(raw_data)
    # data = pd.read_csv("src/data/processed/tm_stats_bundesliga_2026.csv")
    print(data.columns)
    # Load
    load_db(data, teams)

    if csv == True: 
        raw_data.to_csv(f"src/data/raw/raw_tm_stats_{division}_{year}.csv")
        data.to_csv(f"src/data/processed/cleaned_tm_stats_{division}_{year}.csv")
        logger.info("CSV file stored to data folder.")
    logger.info("ETL pipeline finished successfully.")

if __name__=="__main__":
    main()