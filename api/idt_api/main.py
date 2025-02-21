from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from idt_api.api.v1 import user_routes
from idt_api.api.config.settings import settings
from idt_api.infrastructure.setup import setup_infrastructure

async def lifespan(_: FastAPI):
    if settings.ENVIRONMENT != "testing":
        setup_infrastructure() 
    
    yield

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

origins = [
    f"chrome-extension://{settings.EXTENSION_ID}",
]

if settings.ENVIRONMENT == "development":
    origins += ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_routes.router, prefix="/api/v1", tags=["users"])
    
@app.get("/")
def health_check():
    return {"status": "OK"}
