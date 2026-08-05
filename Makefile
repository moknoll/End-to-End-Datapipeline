PROJECT_NAME=football_pipeline

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

db-reset:
	docker compose down -v
	docker compose up -d

run:
	python3 ./src/main.py

pipeline:
	docker compose up -d
	python3 ./src/main.py

clean:
	docker compose down

fclean:
	docker compose down -v
	rm -rf __pycache__
	rm -rf */__pycache__

re:
	make fclean
	make pipeline