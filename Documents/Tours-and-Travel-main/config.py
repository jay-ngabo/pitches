from dotenv import load_dotenv
import os

load_dotenv()


class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://geejay:jayngabo@localhost/blogs'   
  SECRET_KEY= 'twendeTOUR'
  SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):
  pass




class DevConfig(Config):
  DEBUG=True



config_options = {
  'production':ProdConfig,
  'development':DevConfig
}