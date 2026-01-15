from fastapi import FastAPI
from app.api.router import api_router
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.exceptions.validation import (
    request_validation_exception_handler
)

app = FastAPI(title="Auth API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React URL
    allow_credentials=True,
    allow_methods=["*"],  # IMPORTANT
    allow_headers=["*"],  # IMPORTANT
)
app.include_router(api_router)

app.add_exception_handler(
    RequestValidationError,
    request_validation_exception_handler
)
