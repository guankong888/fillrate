import requests
import os
from datetime import datetime, timedelta

API_TOKEN = os.getenv("FLXPOINT_API_TOKEN")
BASE_URL = "https://api.flxpoint.com/api/v2/orders"

def get_recent_orders():
    headers = {
        "X-API-TOKEN": API_TOKEN
    }

    # Filter to past 7 days
    today = datetime.utcnow()
    last_week = today - timedelta(days=7)
    params = {
        "startDate": last_week.strftime('%Y-%m-%d'),
        "endDate": today.strftime('%Y-%m-%d')
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("data", [])
