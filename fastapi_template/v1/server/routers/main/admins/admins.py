from ...base import BaseRouter

router = BaseRouter(prefix="/admins", tags=["admins"])

router.get("")(
    lambda: "Hello from admins"
)
