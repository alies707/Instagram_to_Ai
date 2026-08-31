import os
from urllib.parse import urlencode
import httpx

META_URL = "https://www.facebook.com/v23.0/dialog/oauth"
TOKEN_URL = "https://graph.facebook.com/v23.0/oauth/access_token"


def get_login_url():
    params = {
        "client_id": os.getenv("META_APP_ID"),
        "redirect_uri": os.getenv("META_REDIRECT_URI"),
        "scope": "instagram_basic,instagram_content_publish,pages_show_list",
        "response_type": "code",
    }
    return f"{META_URL}?{urlencode(params)}"

async def exchange_code(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(TOKEN_URL, params={
            "client_id": os.getenv("META_APP_ID"),
            "client_secret": os.getenv("META_APP_SECRET"),
            "redirect_uri": os.getenv("META_REDIRECT_URI"),
            "code": code,
        })
        response.raise_for_status()
        return response.json()
