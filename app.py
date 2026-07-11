from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎓 Computer Engineering Department</h1>
    <h2>WhatsApp Chatbot</h2>
    <p>Server Status: <b>Running ✅</b></p>
    <hr>
    <h3>Main Menu</h3>
    <ol>
        <li>Admission Information</li>
        <li>Faculty Information</li>
        <li>Department Information</li>
        <li>Facilities</li>
        <li>Contact Department</li>
    </ol>
    
    """

if __name__ == "__main__":
    app.run(debug=True)