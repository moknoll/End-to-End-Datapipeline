## Overview
This project implements an end-to-end ETL pipeline for football player data. The pipeline extracts player and team information from transfermarkt, transformrs the raw data into structured datasets, and loads the processed information into a PostgreSQL database.
The goal of this project is to demonstrate practical experience with data engineering workflows, ETL processes, relational database design and containerized application.

## Architecture
The pipeline follows an ETL architecture: 
1. Extract 
- Scrapes team and player for a given division and season from Transfermarkt.
- Uses modular parser components for different daat sources.

2. Transform
- Cleans and validates raw data. 
- Converts values into database-compatible formats.
- Creates relationship between players and teams. 

3. Load 
- Stores processed daat in PostgreSQL
- Provides structured tables for analytical SQL queries.

## Technologies
- Python 
- Pandas 
- BeautifulSoup
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- pgAdmin

## Project Structure

```text
.
├── docker/                # Docker configuration
│   ├── postgres/           # PostgreSQL initialization
│   ├── pgadmin/            # pgAdmin configuration
│   └── python/             # Python Docker image
│
├── src/
│   ├── data/               # Raw and processed datasets
│   ├── loaders/            # Database loading logic
│   ├── models/             # Data models
│   ├── parsers/            # HTML parsing components
│   ├── scrapers/           # Web scraping logic
│   ├── transform/          # Data cleaning and transformation
│   └── utils/              # Helper functions and logging
│
├── main.py                 # ETL pipeline entry point
├── docker-compose.yml      # Multi-container setup
├── Makefile                # Development commands
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Setup

To demonstrate the pipeline is currently setup to scrape bundesliga teams for the 2026 season. To change these: 
1. Open main.py

2. Change these four variables. Set csv=True | False, if you want to store the extrafcted data, clean and raw as a csv file. You can find them in /data.
```python
year=2026
division="bundesliga"
competition="L1"
csv=True

```

1. Clone repo: 
```bash
git clone https://github.com/moknoll/
cd End-to-End-Datapipeline
```

2. Create environment file: 
```bash
cp .env.example .env
```

3. Start the containers: 
```bash
make build
```

## Environment Variables
Example: 
```bash
POSTGRES_USER=moritz
POSTGRES_PASSWORD=password
POSTGRES_DB=football
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

PGADMIN_DEFAULT_EMAIL=admin@football.com
PGADMIN_DEFAULT_PASSWORD=password
```

## Running the Pipeline
Execute the ETL pipeline: 
```bash
make pipeline
```

The pipeline will: 
1. Extract teams of given division ans player data. 
2. Transform and clean datasets.
3. Load tesults into PostreSQL

## Database Schema
The PostgreSQL database consists of two relational tables linked by a foreign key. Each player belongs to exactly one team via the team_id relationship.

### teams

| Column | Type | Description |
|--------|------|-------------|
| team_id | INTEGER | Primary key |
| team_name | TEXT | Unique team identifier (e.g. `fc-bayern-munchen`) |

### players

| Column | Type | Description |
|--------|------|-------------|
| player_id | SERIAL | Primary key |
| team_id | INTEGER | Foreign key referencing `teams.team_id` |
| season | INTEGER | Bundesliga season |
| name | TEXT | Player name |
| number | INTEGER | Jersey number |
| dob | DATE | Date of birth |
| age | INTEGER | Player age |
| country | TEXT | Nationality |
| height | INTEGER | Height in centimeters |
| foot | TEXT | Preferred foot |
| contract | DATE | Contract expiration date |
| joined_date | DATE | Date joined current club |
| signed_from | TEXT | Previous club |
| signing_fee | BIGINT | Transfer fee in euros |
| position | TEXT | Playing position |
| market_value | BIGINT | Market value in euros |

## Example SQL Queries

Top 10 players by market value:
```sql
SELECT name, market_value
FROM players
ORDER BY market_value DESC
LIMIT 10;
```

Average squad value by team:
```sql 
SELECT 
    t.team_name,
    AVG(p.market_value)
FROM players p
JOIN teams t
ON p.team_id = t.team_id
GROUP BY t.team_name;
```

## Future Improvements
- Add analytics dashboard
- Add another scraper for fbref to add more advanced statistics to each player. 

## References
- https://docs.docker.com/guides/postgresql/
- https://docs.sqlalchemy.org/en/20/
- https://ricardoheredia94.medium.com/scraping-transfermarkt-with-python-data-driven-player-recruitment-using-englandschampionship-8ad18b9103fe