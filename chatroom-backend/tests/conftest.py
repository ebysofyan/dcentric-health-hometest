# flake8: NOQA;

import os
import sys
from collections.abc import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

current: str = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(current, "src"))

from database import Database
from main import create_app


@pytest.fixture(scope="session")
def database() -> Generator:
    database = Database(database_url=os.getenv("TEST_DATABASE_URL"))
    yield database


@pytest.fixture
def app(database) -> Generator:
    app: FastAPI = create_app()
    app.container.db.override(database)
    database.create_database()
    yield app
    database.drop_database()


@pytest.fixture
def client(app) -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def db_session(database):
    return database.session
