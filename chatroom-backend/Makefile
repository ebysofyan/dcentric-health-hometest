run-dev:
	uvicorn main:app --host 0.0.0.0 --port 8008 --reload --log-level debug
	# python -B main.py

run-test:
	pytest -vv tests

db-migrate:
	alembic stamp head
	alembic revision

db-upgrade:
	alembic upgrade head

.PHONY: run-dev, run-test, db-migrate, db-upgrade
