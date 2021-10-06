from fastapi_template.v1.server.routers.base import BaseRouter

from fastapi_template.v1.server.routers.main import router as main_router
from fastapi_template.v1.server.routers.root import router as root_router

router = BaseRouter(prefix="/v1")

# Includes all main routes to V1 routers group
router.include_router(main_router, prefix="/main")
router.include_router(root_router, prefix="/root", tags=["root"])

__all__ = [
    "router",
]
