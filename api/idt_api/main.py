from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Test!"}

from fastapi import FastAPI
from idt_api.api.v1 import user_routes
from idt_api.api.config.settings import settings
# from app.dependencies import get_db  # Dependency injection

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(user_routes.router, prefix="/api/v1", tags=["users"])

@app.get("/")
def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("idt_api.main:app", host="127.0.0.1", port=8000, reload=True)
