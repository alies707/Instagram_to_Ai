import requests


class InstagramPublishingService:
    def __init__(self, access_token: str, instagram_id: str, api_version: str = "v23.0"):
        self.access_token = access_token
        self.instagram_id = instagram_id
        self.base_url = f"https://graph.facebook.com/{api_version}"

    def create_image_container(self, image_url: str, caption: str):
        url = f"{self.base_url}/{self.instagram_id}/media"
        payload = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=payload, timeout=30)
        response.raise_for_status()
        return response.json()

    def publish_container(self, creation_id: str):
        url = f"{self.base_url}/{self.instagram_id}/media_publish"
        payload = {
            "creation_id": creation_id,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=payload, timeout=30)
        response.raise_for_status()
        return response.json()
