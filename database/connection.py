from sqlalchemy import create_engine
from urllib.parse import quote_plus


engine_url = "mysql+pymysql://{user}:{password}@{url}:{port}/{db_name}".format(
    user="root",
    password=quote_plus("placer"),
    url="localhost",
    port="3306",
    db_name="rapi",


)

engine_rapi = create_engine(engine_url)

#Sql alchemy se maneja por sesiones
