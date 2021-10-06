from ..base import BaseRouter

router = BaseRouter()

router.get("")(
    lambda: "Hello from admins"
)
