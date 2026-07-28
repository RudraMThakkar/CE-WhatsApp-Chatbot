from flask import Blueprint, request
from chatbot import get_response
from whatsapp import send_whatsapp_message
from config import Config

webhook = Blueprint("webhook", __name__)


@webhook.route("/webhook", methods=["GET"])
def verify():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == Config.VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@webhook.route("/webhook", methods=["POST"])
def receive():

    data = request.get_json()

    print("\n========== Incoming WhatsApp Webhook ==========")
    print(data)

    try:

        if "entry" in data:

            entry = data["entry"][0]

            changes = entry["changes"][0]

            value = changes["value"]

            if "messages" in value:

                message = value["messages"][0]

                phone_number = message["from"]

                message_text = message["text"]["body"]

                print("Phone:", phone_number)

                print("Message:", message_text)

                reply = get_response(phone_number, message_text)

                print("Bot Reply:", reply)

                send_whatsapp_message(phone_number, reply)

    except Exception as e:

        print("Webhook Error:", e)

    return "EVENT_RECEIVED", 200