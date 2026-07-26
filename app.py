from flask import Flask, request
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🎓 Computer Engineering Department</h1>
    <h2>WhatsApp Chatbot</h2>
    <p>Server Status: <b>Running ✅</b></p>

    <hr>

    <h3>Test Your Chatbot</h3>

    <form action="/chat" method="post">
        <input type="text" name="message" placeholder="Type your message">
        <button type="submit">Send</button>
    </form>
    """


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.form["message"]

    bot_reply = get_response(user_message)

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