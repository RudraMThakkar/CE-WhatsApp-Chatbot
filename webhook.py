from flask import Blueprint, request
from chatbot import get_response
from whatsapp import send_whatsapp_message
from config import Config
import json

webhook = Blueprint("webhook", __name__)


# -----------------------------
# Verify Webhook
# -----------------------------
@webhook.route("/webhook", methods=["GET"])
def verify():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == Config.VERIFY_TOKEN:
        print("Webhook Verified Successfully")
        return challenge, 200

    print("Webhook Verification Failed")
    return "Verification failed", 403


# -----------------------------
# Receive Messages
# -----------------------------
@webhook.route("/webhook", methods=["POST"])
def receive():

    data = request.get_json()

    print("\n================= WEBHOOK RECEIVED =================")
    print(json.dumps(data, indent=4))
    print("====================================================\n")

    try:

        if data.get("object") != "whatsapp_business_account":
            print("Not a WhatsApp webhook.")
            return "EVENT_RECEIVED", 200

        for entry in data.get("entry", []):

            for change in entry.get("changes", []):

                value = change.get("value", {})

                # Status updates
                if "statuses" in value:
                    print("Status Update:")
                    print(json.dumps(value["statuses"], indent=4))

                # Incoming messages
                if "messages" in value:

                    message = value["messages"][0]

                    phone_number = message.get("from")
                    message_type = message.get("type")

                    print("Incoming Message Type:", message_type)

                    if message_type == "text":

                        message_text = message["text"]["body"]

                        print("Phone :", phone_number)
                        print("Message :", message_text)

                        reply = get_response(phone_number, message_text)

                        print("Bot Reply :", reply)

                        response = send_whatsapp_message(
                            phone_number,
                            reply
                        )

                        print("Send Message Response :", response)

                    else:
                        print("Unsupported message type:", message_type)

    except Exception as e:
        import traceback

        print("\n******** WEBHOOK ERROR ********")
        traceback.print_exc()
        print("*******************************\n")

    return "EVENT_RECEIVED", 200