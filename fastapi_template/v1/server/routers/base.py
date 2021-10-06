from typing import Any,Callable
from fastapi import (
    APIRouter,
    types,
)

from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)

class BaseRouter(APIRouter):
    
    def api_route(
        self, path: str, *, include_in_schema: bool = True, **kwargs: Any
    ) -> Callable[[types.DecoratedCallable], types.DecoratedCallable]:
        if path.endswith("/"):
            path = path[:-1]

        alternate_path = path + "/"
        super().api_route(alternate_path, include_in_schema=False, **kwargs)
        return super().api_route(
            path, include_in_schema=include_in_schema, **kwargs
        )
  
    def post(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_201_CREATED
        return super().post(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_204_NO_CONTENT
        return super().put(*args, **kwargs)

    def patch(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_204_NO_CONTENT
        return super().put(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if not "status_code" in kwargs:
            kwargs["status_code"] = HTTP_204_NO_CONTENT
        return super().delete(*args, **kwargs)
