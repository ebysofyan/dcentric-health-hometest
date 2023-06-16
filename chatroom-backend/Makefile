run-dev:
	uvicorn main:app --host 0.0.0.0 --port 8008 --reload --log-level debug

db-migrate:
	alembic stamp head
	alembic revision

db-upgrade:
	alembic upgrade head

.PHONY: run-dev, db-migrate, db-upgrade
