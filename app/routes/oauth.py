from fastapi import APIRouter, HTTPException, Request

from app.instagram.oauth import get_login_url, exchange_code

router = APIRouter(prefix="/oauth", tags=["oauth"])


@router.get("/instagram/login")
def instagram_login():
    return {"url": get_login_url()}


@router.get("/instagram/callback")
async def instagram_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Missing OAuth code")
    return await exchange_code(code)
