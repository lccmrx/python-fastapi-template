import os
from pathlib import Path
from dotenv import load_dotenv

from . import supported, util

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

if (env_file:=(BASE_DIR.parent / ".env")).exists():
    load_dotenv(env_file)

class Config:
    __version__ = "0.0.1"
    __env__: supported.SupportedEnv = os.getenv("ENV") or supported.SupportedEnv.DEV
    __basedir__: Path = BASE_DIR
    
    app = util.Key (
        name={"v": os.getenv("APP_NAME"), "p": str, "d": "fastapi-template"},
        description={"v": os.getenv("APP_DESCRIPTION"), "p": str, "d": "This is a template API for FastAPI."},
        port={"v": os.getenv("APP_PORT"), "p": int, "d": 5000},
        https_redirect={"v": os.getenv("APP_HTTPS_REDIRECT"), "p": util.strtobool, "d": "False"},
        trusted_hosts={"v": os.getenv("APP_TRUSTED_HOSTS"), "p": util.array_parser, "d": ""},
        docs_enabled={"v": os.getenv("APP_DOCS_ENABLED"), "p": util.strtobool, "d": "False"},
    )
        
    database = util.Key (
        host={"v": os.getenv("DATABASE_HOST"), "p": str, "d": ""},
        port={"v": os.getenv("DATABASE_PORT"), "p": int, "d": 0},
        user={"v": os.getenv("DATABASE_USER"), "p": str, "d": ""},
        pwd={"v": os.getenv("DATABASE_PWD"), "p": str, "d": ""},
        database={"v": os.getenv("DATABASE_NAME"), "p": str, "d": ""},
        driver={"v": os.getenv("DATABASE_DRIVER"), "p": supported.SupportedDatabaseDriver, "d": supported.SupportedDatabaseDriver.PSQL},
        database_url={"v": os.getenv("DATABASE_URL"), "p": str, "d": ""},
    )
    
    cache = util.Key (
        host={"v": os.getenv("cache_host"), "p": str, "d": ""},
        port={"v": os.getenv("cache_port"), "p": int, "d": 0},
        user={"v": os.getenv("cache_user"), "p": str, "d": ""},
        pwd={"v": os.getenv("cache_pwd"), "p": str, "d": ""},
        cache_database={"v": os.getenv("cache_name"), "p": str, "d": ""},
        driver={"v": os.getenv("cache_driver"), "p": supported.SupportedCacheDriver, "d": supported.SupportedCacheDriver.REDIS},
        cache_url={"v": os.getenv("cache_url"), "p": str, "d": ""},
    )

cfg = Config()

__all__ = [
    "cfg",
    "supported",
]
