build:
	docker compose build

down:
	docker compose down

makemigrations:
	docker compose run --rm app alembic revision --autogenerate -m "$(MSG)"

migrate:
	docker compose run --rm app alembic upgrade head

runserver:
	docker compose up --build -d

test:
	docker compose run --rm app python -m unittest discover -v -s app/tests/$(DIR)
