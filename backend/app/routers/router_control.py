from fastapi import APIRouter
from services.routeros_api import router_reboot, get_interface_list

router = APIRouter(prefix="/router", tags=["Router Control"])

@router.get("/interfaces")
def list_interfaces():
    return get_interface_list()

@router.post("/reboot")
def reboot_router():
    return router_reboot()
