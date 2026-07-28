"""
whatsapp.py

Send WhatsApp messages using WhatsApp Cloud API.
"""

import requests
from config import Config


def send_whatsapp_message(phone_number, message):

    url = (
        f"https://graph.facebook.com/"
        f"{Config.GRAPH_API_VERSION}/"
        f"{Config.PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {Config.ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("WhatsApp API Status:", response.status_code)
    print(response.text)

    return response