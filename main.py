import os
import yaml
from fastapi import FastAPI
from yaml.loader import SafeLoader
from dotenv import load_dotenv

load_dotenv()

TRAEFIK_CONFIG_DIRECTORY = str(os.getenv('TRAEFIK_CONFIG_DIRECTORY'))
TRAEFIK_DYNAMIC_CONFIG = str(os.getenv('TRAEFIK_DYNAMIC_CONFIG'))

app = FastAPI()


@app.get("/")
async def root():
    data = ''
    with open(TRAEFIK_DYNAMIC_CONFIG) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data
