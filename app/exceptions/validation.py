from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def request_validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = {}

    for error in exc.errors():
        field = error["loc"][-1]
        errors[field] = error["msg"]

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": False,
            "message": "Validation error",
            "errors": errors
        }
    )
