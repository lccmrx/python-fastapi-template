from fastapi import Request
from ..base import BaseRouter

health_router = BaseRouter(prefix="/health")

@health_router.get("")
def handle_health_check(request: Request):
    url_list = [
        {"path": route.path, "name": route.name} for route in request.app.routes
    ]
    return url_list
