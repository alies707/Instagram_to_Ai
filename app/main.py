from fastapi import FastAPI

app = FastAPI(
    title="Instagram AI Manager",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "instagram-ai-manager"
    }
