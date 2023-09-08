import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def fetchUserData(username):
    url = os.getenv("API_KEY")
    response = requests.get(url)
    data = json.loads(response.text)
    return data
