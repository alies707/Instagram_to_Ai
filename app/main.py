from fastapi import FastAPI

from app.routes.instagram import router as instagram_router
from app.routes.publish import router as publish_router
from app.routes.webhook import router as webhook_router

app = FastAPI(
    title="Instagram AI Manager",
    version="0.2.0"
)

app.include_router(instagram_router)
app.include_router(publish_router)
app.include_router(webhook_router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "instagram-ai-manager"
    }
