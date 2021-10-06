import copy
from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional

from fastapi import FastAPI, APIRouter, Request
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
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

def create_custom_openapi(app: FastAPI):
    def cust_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            description="This is a very custom OpenAPI schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }

        for path in {x for x in openapi_schema["paths"] if x.endswith("$")}:
            openapi_schema["paths"][path[:-1]] =openapi_schema["paths"][path]
            del openapi_schema["paths"][path]

        app.openapi_schema = openapi_schema

        return app.openapi_schema

    return cust_openapi
