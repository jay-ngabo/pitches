import os

class Config:


   '''
   General configuration parent class
   '''
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SECRET_KEY=os.environ.get('SECRET_KEY')
   UPLOADED_PHOTOS_DEST ='app/static/photos'
   # simple mde configuration
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True

   #mail cconfiguration


   MAIL_SERVER= 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS=True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):


   # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/watchlist_test'
   pass


class ProdConfig(Config):


   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/watchlist'
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

   '''
   Development  configuration child class
   Args:

       Config: The parent configuration class with General configuration settings

   '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/pitches'
   DEBUG = True



config_options = {


'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

