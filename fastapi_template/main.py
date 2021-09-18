from fastapi import FastAPI, APIRouter
from fastapi.middleware import (
    cors,
    trustedhost,
    httpsredirect
)
from fastapi_template.infra.core.config import cfg
from fastapi_template.infra.utils import docs

def startup_handler(
    app: FastAPI
) -> callable:
    def startup():
        app.cfg = cfg

    return startup

def shutdown_handler(
    app: FastAPI
) -> callable:
    async def shutdown():
        print("Shutting down...")
    
    return shutdown

def include_global_middlewares(
    app: FastAPI
) -> None:
    # CORS Middleware Configuration
    from fastapi_template.infra.core.config.supported import SupportedEnv
    if cfg.__env__ != SupportedEnv.DEV:
        app.add_middleware(
            cors.CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=False,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        # HTTP to HTTPS Redirect Middleware Configuration
        (lambda x: app.add_middleware(httpsredirect.HTTPSRedirectMiddleware) if x else None) (cfg.app.https_redirect)
        # Trusted Host Middleware Configuration
        app.add_middleware(
            trustedhost.TrustedHostMiddleware,
            allowed_hosts=cfg.app.trusted_hosts
        )

def get_app(
    
):
    app = FastAPI(
        title=cfg.app.name or "FastAPI Template",
        openapi_url=None,
        swagger_url=None,
        redoc_url=None,
    )
    root_router = APIRouter(prefix="/api")
    
    from fastapi_template.v1.server.routers import router as v1_router
    docs.create_versioned_docs(v1_router, cfg.app.docs_enabled, **{"title": "API Version 1", "description": "API Version 1", "version": "v1", "root_prefix": root_router.prefix})
    root_router.include_router(v1_router)
    
    app.include_router(root_router)
    app.add_event_handler("startup", startup_handler(app))
    app.add_event_handler("shutdown", shutdown_handler(app))
    include_global_middlewares(app)
    return app

app = get_app()

def main():
    import uvicorn
    
    uvicorn.run(
        "fastapi_template.main:app",
        port=cfg.app.port,
        reload=True
    )
