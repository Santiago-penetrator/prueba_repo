from fastapi import APIRouter, Response,FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from models.user_models import UserC
from Modules.user_modules import UserMo
from responses.globalResponse import error_response,succes_response,http_exeption_handler

router_user = APIRouter(
    prefix="/api/user",
    tags=["user"],
)

@router_user.post(
    path="/create",
    summary="create user",
)
async def create_user(user: UserC):
    try:
        user = await UserMo.create_user(user)
        return succes_response(data=user,status=201,message="usuario encontrado correctamente")
    except Exception as ex:
        return error_response(message="Error en create_user", ex=str(ex), status_code=500)
    
@router_user.get(
    path="/login",
    summary="login user",
)
async def login_user(email: str, password: str):
    try:
        user = await UserMo.login_user(email, password)
        return succes_response(data=user,status=200,message="usuario logeado correctamente")
    except HTTPException as ex:
        return HTTPException(status_code=ex.status_code, detail=ex.detail)
    except Exception as ex:
        return error_response(message="Error en login_user", ex=str(ex), status_code=500)