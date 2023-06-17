# flake8: NOQA;

import os
import sys

from dotenv import load_dotenv

current: str = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current, "src"))

from deps_container import Container
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from routes.chat_room_routes import router as chat_room_router
from routes.chat_routes import router as chat_router
from routes.user_routes import router as user_router
from routes.ws_routes import router as ws_router

origins = [
    "http://localhost:19000",
]


def create_app() -> FastAPI:
    load_dotenv()
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.container = container
    app.include_router(chat_room_router)
    app.include_router(chat_router)
    app.include_router(user_router)
    app.include_router(ws_router)
    return app


app = create_app()
