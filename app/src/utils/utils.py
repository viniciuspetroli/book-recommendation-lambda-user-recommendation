import json
import requests
from aws_lambda_powertools import Logger, Tracer

logger = Logger()

api_key = "AIzaSyAUHuMkuWch8hZnzA2308ga7oX-rkxf9SM"

def call_gemini_api(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Erro ao chamar a API Gemini: {str(e)}")
        return None