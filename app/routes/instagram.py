from fastapi import APIRouter

from app.instagram.account import InstagramAccountService

router = APIRouter(prefix="/instagram", tags=["Instagram"])


@router.get("/account")
def account_info(instagram_id: str, access_token: str):
    service = InstagramAccountService(access_token)
    return service.get_account_info(instagram_id)


@router.get("/pages")
def pages(access_token: str):
    service = InstagramAccountService(access_token)
    return service.get_managed_pages()
