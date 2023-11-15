from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from models.user_models import UserM,UserC
from Schemas.user_schemas import UserS
from database.connection import engine_rapi
from fastapi import HTTPException
from responses.user_response import response_create_user

class UserMo:
    @classmethod
    async def _sqlalchemy_to_dict(cls,obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.colum_attrs}
    
    @classmethod
    async def _get_session_(cls):
        Session = sessionmaker(bind=engine_rapi)
        session = Session()
        return session
    
    @classmethod
    async def create_user(cls,user: UserC):
        try:
            session = await cls._get_session_()
            session.add(user)
            session.commit()
            user_data = await cls._sqlalchemy_to_dict(user)
            return response_create_user(**user_data)
        except Exception as ex:
            session.rollback
            raise Exception(ex)
        finally:
            session.close() 
            

    @classmethod
    async def login_user(cls,email:str,password:str):
        try:
            session = await cls._get_session_()
            user = session.query(UserS).filter(UserS.email==email,UserS.password==password).first()
            if user:
                user_dict = await cls._sqlalchemy_to_dict(user)
                return response_create_user(**user_dict)
            raise HTTPException(status_code=404, detail="User not found")
        except HTTPException:
            raise
        except Exception as ex:
            print(f"Error en login_user {ex}")
            session.rollback
            raise Exception(ex)
        finally:
            session.close()