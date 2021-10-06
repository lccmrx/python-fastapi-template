from enum import Enum

class SupportedEnv(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"
    
class SupportedDatabaseDriver(str, Enum):
    PSQL = "psql"
    MYSQL = "mysql"
    
class SupportedCacheDriver(str, Enum):
    REDIS = "redis"
