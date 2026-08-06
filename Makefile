COMPOSE = docker compose

up:
	$(COMPOSE) up

# Erstes Starten
build:
	$(COMPOSE) up --build 

# Logs verfolgen 
logs:
	$(COMPOSE) logs -f 

# In den python container wechseln 
shell:
	$(COMPOSE) exec python bash

down:
	$(COMPOSE) down

rebuild:
	$(COMPOSE) down
	$(COMPOSE) build --no-cache
	$(COMPOSE) up

pipeline:
	$(COMPOSE) exec python python main.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

db-reset:
	$(COMPOSE) down -v
	$(COMPOSE) up --build

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run:
	python3 main.py

lint:
	ruff check .

format:
	black .

.PHONY: up down build rebuild logs shell clean pipeline