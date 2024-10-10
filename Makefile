start-dev: start-dev-db start-dev-server

start-dev-db:
	docker-compose up -d

start-dev-server:
	source server/venv/bin/activate && fastapi dev server/app/main.py
