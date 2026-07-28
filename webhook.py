from flask import Blueprint, request
from chatbot import get_response

webhook = Blueprint("webhook", __name__)

VERIFY_TOKEN = "ce_chatbot_verify_token"


@webhook.route("/webhook", methods=["GET"])
def verify():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@webhook.route("/webhook", methods=["POST"])
def receive():

    data = request.get_json()

    print("Incoming WhatsApp Message:")
    print(data)

    return "EVENT_RECEIVED", 200