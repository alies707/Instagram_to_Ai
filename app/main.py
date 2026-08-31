from fastapi import FastAPI

from app.routes.instagram import router as instagram_router
from app.routes.publish import router as publish_router
from app.routes.webhook import router as webhook_router
from app.routes.oauth import router as oauth_router

app = FastAPI(
    title="Instagram AI Manager",
    version="0.3.0"
)

app.include_router(instagram_router)
app.include_router(publish_router)
app.include_router(webhook_router)
app.include_router(oauth_router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "instagram-ai-manager"
    }
