from app.instagram.client import InstagramGraphClient

class InstagramPublisher:
    def __init__(self, access_token: str, account_id: str):
        self.client = InstagramGraphClient(access_token)
        self.account_id = account_id

    async def publish(self, image_url: str, caption: str):
        return await self.client.publish_image(
            self.account_id,
            image_url,
            caption,
        )
