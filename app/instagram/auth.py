import requests


class MetaAuth:
    def __init__(self, app_id: str, app_secret: str, redirect_uri: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri

    def exchange_code(self, code: str):
        url = "https://graph.facebook.com/v23.0/oauth/access_token"
        params = {
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def exchange_long_lived_token(self, short_token: str):
        url = "https://graph.facebook.com/v23.0/oauth/access_token"
        params = {
            "grant_type": "fb_exchange_token",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "fb_exchange_token": short_token,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
