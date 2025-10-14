from fastapi import APIRouter
from services.daloradius_db import get_active_users

router = APIRouter(prefix="/nas", tags=["NAS System"])

@router.get("/active-users")
def list_active_users():
    return get_active_users()
