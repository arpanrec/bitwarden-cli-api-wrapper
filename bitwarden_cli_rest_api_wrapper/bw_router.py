# https://127.0.0.1:8200/v1/secret/data/my-secret

from fastapi import APIRouter
from bitwarden_cli_rest_api_wrapper import cli_ops

router = APIRouter()


@router.get("/status", tags=["bw"], description="Get secret data")
async def get_status():
    return cli_ops.get_current_status()
