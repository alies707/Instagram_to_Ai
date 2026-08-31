import requests

class InstagramPublisher:
    def __init__(self, access_token: str, account_id: str):
        self.access_token = access_token
        self.account_id = account_id

    def create_media_container(self, image_url: str, caption: str):
        return {
            "image_url": image_url,
            "caption": caption,
            "status": "ready_for_meta_api"
        }

    def publish(self, creation_id: str):
        return {
            "creation_id": creation_id,
            "status": "pending_api_connection"
        }
