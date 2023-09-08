import requests
import json
from dotenv import load_dotenv
import os
import time
import pandas as pd

load_dotenv()

api_key = os.getenv('API_KEY')
base_url = 'https://api.stackexchange.com/2.3/users/'

def fetchUserData(user_ids):
    user_data_list = []
    
    for user_id in user_ids:
        user_data = {}
        
        try:
            # Fetch basic user information
            response = requests.get(f"{base_url}{user_id}?site=stackoverflow&key={api_key}")
            basic_data = json.loads(response.text)
            user_data['basic'] = basic_data.get('items', [])[0] if 'items' in basic_data else {}
            time.sleep(1 / 30)
            
            # Fetch user's questions
            response = requests.get(f"{base_url}{user_id}/posts?site=stackoverflow&key={api_key}")
            posts_data = json.loads(response.text)
            user_data['posts'] = posts_data.get('items', [])
            time.sleep(1 / 30)

            # Fetch tags user are active in
            response = requests.get(f"{base_url}{user_id}/tags?site=stackoverflow&key={api_key}")
            tags_data = json.loads(response.text)
            user_data['tags'] = tags_data.get('items', [])
            time.sleep(1 / 30)

            # Fetch user's reputation
            response = requests.get(f"{base_url}{user_id}/reputation?site=stackoverflow&key={api_key}")
            reputation_data = json.loads(response.text)
            user_data['reputation'] = reputation_data.get('items', [])
            time.sleep(1 / 30)
        
        except Exception as e:
            print(e, f"error for user_id: {user_id}") 
            continue

        user_data_list.append(user_data)

    df = pd.DataFrame(user_data_list)
    return df
