import requests
import json
from dotenv import load_dotenv
import os
import time
import pandas as pd

load_dotenv()

api_key = os.getenv('API_KEY')
base_url = 'https://api.stackexchange.com/2.3/users/'

def fetchUserID(page=1, sort='creation', order='desc'):
    try:
        params = {
        'page': page,
        'pagesize': 100,
        'sort': sort,
        'order': order,
        'site': 'stackoverflow',
        'key': api_key
    }
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)
        user_ids = [user['user_id'] for user in data.get('items', [])]
        time.sleep(1 / 30)
        return user_ids
    
    except Exception as e:
        print(e)
        return []

