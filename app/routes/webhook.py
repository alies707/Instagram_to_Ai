from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhook", tags=["Webhook"])


@router.get("/instagram")
def verify_webhook(mode: str, challenge: str, verify_token: str):
    return {"challenge": challenge, "mode": mode}


@router.post("/instagram")
async def receive_webhook(request: Request):
    payload = await request.json()
    return {"received": True, "data": payload}
