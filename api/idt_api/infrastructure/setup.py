from fastapi import FastAPI
from idt_api.infrastructure.db.setup import setup_db

def setup_infrastructure(app: FastAPI):
    setup_db(app.state.settings.DB_URL, app.state.settings.DB_USERNAME, app.state.settings.DB_PASSWORD)

    return app