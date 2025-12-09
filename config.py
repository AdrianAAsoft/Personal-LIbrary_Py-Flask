import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    host = os.getenv("HOST")
    port = os.getenv("Puerto", 6505)
