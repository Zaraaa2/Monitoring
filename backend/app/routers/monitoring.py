from fastapi import APIRouter
from services.snmp_client import get_router_stats

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])

@router.get("/router")
def router_status():
    return get_router_stats()
