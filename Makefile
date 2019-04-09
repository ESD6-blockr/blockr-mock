black:
	docker-compose exec backend bash -c "black . -l 120"

flake8:
	docker-compose exec backend bash -c "flake8"

dev:
	@docker-compose up --build

makemigrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate

shell:
	docker-compose run --rm backend python manage.py shell
