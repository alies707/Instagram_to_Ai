from fastapi import APIRouter

router = APIRouter(prefix="/publish")


@router.post("/image")
def publish_image(image_url: str, caption: str):
    return {
        "status": "queued",
        "image_url": image_url,
        "caption": caption
    }
