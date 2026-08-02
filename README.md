# 🎓 CE Admission Chatbot

The chatbot helps students instantly access admission-related information through a web interface and is designed for future WhatsApp integration.

---

## 📌 Features

- 📖 Admission Information
- 👨‍🏫 Faculty Details
- 🏛 Department Information
- 🧾 Document Requirements
- 🧪 Laboratory Information
- 📞 Contact Information
- 💾 SQLite Database
- 🔄 State-Based Conversation Flow
- 🌐 Flask Web Application
- 📱 WhatsApp Cloud API Integration (In Progress)

---

## 🛠 Tech Stack

- Python 3
- Flask
- SQLite
- HTML
- CSS
- WhatsApp Cloud API
- Ngrok (Development)

---

## 📂 Project Structure

```
CE-Admission-Chatbot/
│
├── app.py
├── chatbot.py
├── config.py
├── database.py
├── state_manager.py
├── webhook.py
├── whatsapp.py
├── responses.py
├── chatbot.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/CE-Admission-Chatbot.git
```

```bash
cd CE-Admission-Chatbot
```

### Install Dependencies

```bash
pip install flask requests
```

### Run Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 💬 Main Menu

```
1. Admission Information

2. Faculty Details

3. Department Information

4. Laboratory Facilities

5. Contact Information
```

---

## 🗂 Database

The chatbot uses SQLite to store:

- Admission Details
- Faculty Information
- Department Information
- Laboratory Details
- Contact Information
- Required Documents

---

## 📱 WhatsApp Integration

This project is designed to work with the WhatsApp Cloud API.

Current Status:

- ✅ Webhook Verification
- ✅ API Integration
- ✅ Message Processing Logic
- 🔄 Deployment & Incoming Message Testing

---

## 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/home.png
screenshots/chat.png
```

---

## 🎯 Future Improvements

- AI-powered responses
- Voice Support
- Multi-language Support
- Student Login
- Admin Dashboard
- Live WhatsApp Deployment

---

## 👨‍💻 Developed By

**Your Name**

Computer Engineering Department

Final Year Project

---

## 📄 License

This project is developed for educational purposes.
