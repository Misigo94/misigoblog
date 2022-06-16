import os
import re

class Config:
#     DEBUG=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
   


 # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://martin4:password@localhost:5432/myblogdb'

    
    
        
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
           SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)

configurations = {"production":ProdConfig, "development":DevConfig}