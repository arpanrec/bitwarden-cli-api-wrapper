# https://127.0.0.1:8200/v1/secret/data/my-secret

from fastapi import APIRouter

router = APIRouter()


@router.get("/{path}", tags=["bw"], description="Get secret data")
async def read_users(path: str = "abc"):
    return [{"username": "Rick"}, {"username": path}]
