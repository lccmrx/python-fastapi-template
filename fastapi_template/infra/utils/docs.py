import copy
from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional

from fastapi import APIRouter, Request
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import HTMLResponse

custom_openapi: DefaultDict[str, Optional[Dict[str, Any]]] = defaultdict(lambda: None)

def create_versioned_docs(router: APIRouter, docs_enabled: bool = True, **info) -> None:
    prefix = info.get('root_prefix', None) + router.prefix

    if not docs_enabled:
        return

    @router.get("/openapi.json", include_in_schema=False, name=f"{prefix}_openapi")
    async def get_openapi_json(request: Request) -> dict:
        version = request.url.path.strip("/").split("/")[1]
        if custom_openapi[version] is None:
            custom_openapi[version] = copy.deepcopy(request.app.openapi())
            for key, value in info.items():
                custom_openapi[version]['info'][key] = value

            # Remove other version tags on openapi schema.
            for path in custom_openapi[version]["paths"].copy():
                if not path.startswith(prefix):
                    del custom_openapi[version]["paths"][path]

        return custom_openapi[version]

    @router.get("/docs", include_in_schema=False, name=f"{prefix}_swagger")
    async def get_swagger(request: Request) -> HTMLResponse:
        print(prefix)
        return get_swagger_ui_html(
            openapi_url=f"{prefix}/openapi.json",
            title=request.app.title + " - Swagger UI",
        )

    @router.get("/redoc", include_in_schema=False, name=f"{prefix}_redoc")
    async def redoc_html(request: Request) -> HTMLResponse:
        return get_redoc_html(
            openapi_url=f"{prefix}/openapi.json",
            title=request.app.title + " - ReDoc"
        )
