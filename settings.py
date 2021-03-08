from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
MY_JWT_SECRET_KEY = os.getenv("MY_JWT_SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")