import requests


class InstagramAPI:
    def __init__(self, access_token: str, api_version: str = "v23.0"):
        self.access_token = access_token
        self.base_url = f"https://graph.facebook.com/{api_version}"

    def get_account(self, instagram_account_id: str):
        url = f"{self.base_url}/{instagram_account_id}"
        params = {
            "fields": "id,username,name,profile_picture_url",
            "access_token": self.access_token,
        }
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def create_media_container(self, instagram_account_id: str, image_url: str, caption: str):
        url = f"{self.base_url}/{instagram_account_id}/media"
        data = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=data, timeout=30)
        response.raise_for_status()
        return response.json()

    def publish_media(self, instagram_account_id: str, creation_id: str):
        url = f"{self.base_url}/{instagram_account_id}/media_publish"
        data = {
            "creation_id": creation_id,
            "access_token": self.access_token,
        }
        response = requests.post(url, data=data, timeout=30)
        response.raise_for_status()
        return response.json()
