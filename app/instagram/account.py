import requests


class InstagramAccountService:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def get_managed_pages(self):
        url = "https://graph.facebook.com/v23.0/me/accounts"
        params = {
            "fields": "name,access_token,instagram_business_account",
            "access_token": self.access_token,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_account_info(self, instagram_id: str):
        url = f"https://graph.facebook.com/v23.0/{instagram_id}"
        params = {
            "fields": "id,username,name,profile_picture_url",
            "access_token": self.access_token,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
