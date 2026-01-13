from fastapi import FastAPI
from app.api.router import api_router
from fastapi.exceptions import RequestValidationError

from app.exceptions.validation import (
    request_validation_exception_handler
)

app = FastAPI(title="Auth API")
app.include_router(api_router)

app.add_exception_handler(
    RequestValidationError,
    request_validation_exception_handler
)
