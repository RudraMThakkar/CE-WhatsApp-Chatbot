from flask import Flask, render_template, request
from chatbot import get_response
from database import initialize_database
from webhook import webhook

# Initialize database
initialize_database()

app = Flask(__name__)

app.register_blueprint(webhook)

# Store chat history (for web testing only)
chat_history = []


@app.route("/")
def home():
    return render_template("index.html", chat_history=chat_history)


@app.route("/chat", methods=["POST"])
def chat():

    user_id = "web_user"

    user_message = request.form["message"].strip()

    if user_message == "":
        return "", 204

    bot_reply = get_response(user_id, user_message)

    # Save user message
    chat_history.append({
        "sender": "user",
        "text": user_message
    })

    # Save bot message
    chat_history.append({
        "sender": "bot",
        "text": bot_reply
    })

    # Return only the bot reply
    return bot_reply


if __name__ == "__main__":
    app.run(debug=True)