from fastapi import FastAPI
from idt_api.api.v1 import user_routes
from idt_api.api.config.settings import settings
from idt_api.infrastructure.setup import setup_infrastructure

async def lifespan(app: FastAPI):
    setup_infrastructure() 
    yield

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)
app.state.settings = settings

app.include_router(user_routes.router, prefix="/api/v1", tags=["users"])
    
@app.get("/")
def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("idt_api.main:app", host="127.0.0.1", port=8000, reload=True)
