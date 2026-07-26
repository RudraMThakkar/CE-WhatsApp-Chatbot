from flask import Flask, render_template, request
from chatbot import get_response
from database import initialize_database

# Create database
initialize_database()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_id = "web_user"

    user_message = request.form["message"]

    bot_reply = get_response(user_id, user_message)

    return f"""
    <h2>🤖 Chatbot Reply</h2>

    <p><b>You:</b> {user_message}</p>

    <p><b>Bot:</b></p>

    <pre>{bot_reply}</pre>

    <br>

    <a href="/">⬅ Back</a>
    """


if __name__ == "__main__":
    app.run(debug=True)