from ..base import BaseRouter

router = BaseRouter()

router.get("/me")(
    lambda: "hello"
)

router.get("")(
    lambda: "hello"
)

router.get("/{id}")(
    lambda: "hello"
)

router.head("/{id}")(
    lambda: "hello"
)

router.post("")(
    lambda: "hello"
)

router.put("/{id}")(
    lambda: "hello"
)

router.patch("/{id}")(
    lambda: "hello"
)

router.delete("/{id}")(
    lambda: "hello"
)

router.get("/ws/{id}")(
    lambda: "Hello from ws"
)
