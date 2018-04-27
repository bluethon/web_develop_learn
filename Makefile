venv:
	docker start web_dev
	docker exec -it -w /app web_dev bash

down:
	docker-compose down

up:
	docker-compose up

c:
	pip-compile

s:
	pip-sync
