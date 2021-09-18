from ..base import BaseRouter
from .health import health_router

router = BaseRouter()
router.include_router(health_router)

__all__ = [
    "router",
]
