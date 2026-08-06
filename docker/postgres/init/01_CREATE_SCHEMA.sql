CREATE TABLE teams (
    team_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_name TEXT NOT NULL
);

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    team_id INTEGER NOT NULL REFERENCES teams(team_id),
    season INTEGER NOT NULL,
    name TEXT NOT NULL,
    number INTEGER,
    dob DATE,
    age INTEGER,
    country TEXT,
    height INTEGER,
    foot TEXT,
    contract DATE,
    joined_date DATE,
    signed_from TEXT,
    signing_fee BIGINT,
    position TEXT,
    market_value BIGINT
);