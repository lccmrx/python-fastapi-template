from ..base import BaseRouter
from .admins import router as admins_router
from .users import router as users_router

router = BaseRouter()

router.include_router(admins_router, prefix="/admins", tags=["admins"])
router.include_router(users_router, prefix="/users", tags=["users"])

__all__ = [
    "router",
]
