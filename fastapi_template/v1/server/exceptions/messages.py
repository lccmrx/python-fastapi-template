from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_409_CONFLICT,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)

class DefaultErr(Exception):
    """Base class for all exceptions in this module."""
    def __init__(self, 
        message = "An Error Occured",
        *,
        friendly_message = "Ocorreu um erro",
        status_code = HTTP_500_INTERNAL_SERVER_ERROR,
        headers = {"X-Error": "An Error Occured"}
    ):
        self.message = message
        self.friendly_message = friendly_message
        self.status_code = status_code
        self.headers = headers

class ErrBadRequest(DefaultErr):
    def __init__(self, 
        message = "Bad Request",
        *,
        friendly_message = "Requisição mal-formada",
        status_code = HTTP_400_BAD_REQUEST,
        headers = {"X-Error": "Bad Request"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrUnauthorized(DefaultErr):
    def __init__(self, 
        message = "Unauthorized Access",
        *,
        friendly_message = "Acesso não autorizado",
        status_code = HTTP_401_UNAUTHORIZED,
        headers = {"X-Error": "Unauthorized Access"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrForbidden(DefaultErr):
    def __init__(self, 
        message = "Access Forbidden",
        *,
        friendly_message = "Acesso negado",
        status_code = HTTP_403_FORBIDDEN,
        headers = {"X-Error": "Access Forbidden"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrNotFound(DefaultErr):
    def __init__(self, 
        message = "Not Found",
        *,
        friendly_message = "Não encontrado",
        status_code = HTTP_404_NOT_FOUND,
        headers = {"X-Error": "Not Found"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrRequestTimedOut(DefaultErr):
    def __init__(self, 
        message = "Request Timed Out",
        *,
        friendly_message = "Requisição levou muito tempo",
        status_code = HTTP_408_REQUEST_TIMEOUT,
        headers = {"X-Error": "Request Timed Out"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrConflict(DefaultErr):
    def __init__(self, 
        message = "Conflict",
        *,
        friendly_message = "Conflito",
        status_code = HTTP_409_CONFLICT,
        headers = {"X-Error": "Conflict"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrUnprocessableEntity(DefaultErr):
    def __init__(self, 
        message = "Unprocessable Entity",
        *,
        friendly_message = "Entidade não processável",
        status_code = HTTP_422_UNPROCESSABLE_ENTITY,
        headers = {"X-Error": "Unprocessable Entity"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrInternalServer(DefaultErr):
    def __init__(self, 
        message = "Internal Server Error",
        *,
        friendly_message = "Erro interno",
        status_code = HTTP_500_INTERNAL_SERVER_ERROR,
        headers = {"X-Error": "Internal Server Error"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)

class ErrServiceUnavailable(DefaultErr):
    def __init__(self, 
        message = "Service Unavailable",
        *,
        friendly_message = "Serviço indisponível",
        status_code = HTTP_503_SERVICE_UNAVAILABLE,
        headers = {"X-Error": "Service Unavailable"}
    ):
        super().__init__(message, friendly_message = friendly_message, status_code = status_code, headers = headers)
