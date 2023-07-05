import requests
from dotenv import load_dotenv
import os 

load_dotenv()
load_dotenv("/home/userConnect/Dowell-Original-AI/.env")

# api_key = os.getenv("API_KEY")
api_key = os.getenv('API_KEY')
print(api_key)

def originalAI(content,title):
    url = "https://api.originality.ai/api/v1/scan/ai"

    payload = {
        "content": content,
        "title": title,
        "aiModelVersion": "1"
    }
    headers = {
        "X-OAI-API-KEY": api_key,
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text