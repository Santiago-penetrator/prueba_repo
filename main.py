from fastapi import FastAPI,HTTPException
from pydantic import ValidationError
from responses.globalResponse import http_exeption_handler,validation_exeption_handler
from config.config_cors import add_cors_middleware


app = FastAPI()


app.add_exeption_handler(HTTPException,http_exeption_handler)
app.add_exeption_handler(ValidationError,validation_exeption_handler)
add_cors_middleware(app)