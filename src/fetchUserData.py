import requests
import json
from dotenv import load_dotenv

def fetchUserData(username):
    url = "https://api.github.com/users/" + username
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
