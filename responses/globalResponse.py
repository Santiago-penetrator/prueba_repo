from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from typing import Any

def succes_response(data:Any,status:int, message:str = "Operation succesful") -> JSONResponse:
    return JSONResponse(content={"Success":True, "Message":message, "Data":jsonable_encoder(data)},status_code=status)

def error_response(message:str, ex:str, status_code:int = 400) -> JSONResponse:
    return JSONResponse(content={"Success":True, "Message":message, "Error":ex},status_code=status_code)

def http_exeption_handler(request, exc: HTTPException) -> JSONResponse:
    return error_response(str(exc.detail),exc.status_code)

def validation_exeption_handler(request, exc: ValidationError) -> JSONResponse:
    return error_response(str(exc.errors()),422)