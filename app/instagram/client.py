import os
import httpx

class InstagramGraphClient:
    def __init__(self, token: str):
        self.token = token
        self.base = "https://graph.facebook.com/v23.0"

    async def publish_image(self, instagram_id: str, image_url: str, caption: str):
        async with httpx.AsyncClient() as client:
            container = await client.post(
                f"{self.base}/{instagram_id}/media",
                params={"image_url": image_url, "caption": caption, "access_token": self.token},
            )
            container.raise_for_status()
            return container.json()
