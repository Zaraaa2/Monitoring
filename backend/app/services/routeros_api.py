from librouteros import connect
from app import config

def _connect():
    try:
        api = connect(
            username=config.ROUTER_USER,
            password=config.ROUTER_PASS,
            host=config.ROUTER_IP
        )
        return api
    except Exception as e:
        return None

def get_interface_list():
    try:
        api = _connect()
        if not api:
            return {"error": "Cannot connect to router"}
        interfaces = [i for i in api(cmd="/interface/print")]
        return {"interfaces": interfaces}
    except Exception as e:
        return {"error": str(e)}

def router_reboot():
    try:
        api = _connect()
        if not api:
            return {"error": "Cannot connect to router"}
        api(cmd="/system/reboot")
        return {"message": "Router reboot command sent"}
    except Exception as e:
        return {"error": str(e)}
