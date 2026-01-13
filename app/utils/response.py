from fastapi import status
from fastapi.responses import JSONResponse
from typing import Any, Optional


def send_success_response(
    message: str,
    status_code: int = status.HTTP_200_OK
):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": True,
            "message": message
        }
    )

def send_records_response(
    message: str,
    data: Any,
    total_count: Optional[int] = None,
    status_code: int = status.HTTP_200_OK
):
    response = {
        "status": True,
        "message": message,
        "data": data
    }

    if total_count is not None:
        response["totalCount"] = total_count

    return JSONResponse(
        status_code=status_code,
        content=response
    )

def send_error_response(
    message: str,
    errors: Any = None,
    status_code: int = status.HTTP_400_BAD_REQUEST
):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": False,
            "message": message,
            "errors": errors
        }
    )
