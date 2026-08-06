from sqlalchemy import create_engine 
import pandas as pd 

class PostgresLoader: 
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)

    def load_teams(self, teams: list):
        team_data = pd.DataFrame(
            [
                {
                    "team_name": team.name,
                }
                for team in teams
            ]
        )

        team_data.to_sql("teams",self.engine,if_exists="append",index=False,)
    
    def get_team_mapping(self) -> dict:
        query = """
            SELECT team_name, team_id
            FROM teams;
        """

        df = pd.read_sql(query,self.engine)

        return dict(zip(df["team_name"],df["team_id"]))

    def load_players(self, df: pd.DataFrame): 
        df.to_sql("players", self.engine, if_exists="append", index=False)