from enum import Enum
from .permissions import Permissions

class Roles(Enum):
    GUEST = {
        "description": "", 
        "default_permissions": [
            Permissions.READ,
        ]
    }
    
    USER = {
        "description": "", 
        "default_permissions": [
            Permissions.READ,
            Permissions.CREATE,
        ]
    }
    
    ADMIN = {
        "description": "", 
        "default_permissions": [
            Permissions.READ,
            Permissions.CREATE,
            Permissions.EDIT,
        ]
    }
    
    SUPER_ADMIN = {
        "description": "", 
        "default_permissions": [
            Permissions.READ,
            Permissions.CREATE,
            Permissions.EDIT,
            Permissions.REMOVE,
        ]
    }
