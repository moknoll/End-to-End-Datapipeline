import os
import pandas as pd
from dotenv import load_dotenv
from src.loaders.db_loader import PostgresLoader

def load_db(data: pd.DataFrame, teams: str) -> None: 
    """Get env from .env file and load data in databse"""

    URL = get_url()
    loader = PostgresLoader(URL)
    loader.load_teams(teams)
    team_mapping = loader.get_team_mapping()
    data["team_id"] = data["team"].map(team_mapping)
    del data["team"]
    loader.load_players(data)
    return

def get_url() -> str: 
    load_dotenv()

    USER = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB = os.getenv("POSTGRES_DB")
    HOST = os.getenv("HOST")
    PORT = os.getenv("POSTGRES_PORT")

    URL = (f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")
    return URL