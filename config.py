import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ce_chatbot_secret_key")

    # WhatsApp Cloud API
    ACCESS_TOKEN = os.getenv(
        "WHATSAPP_ACCESS_TOKEN",
        "EAAahMmMvp5kBSYzEJO6Xnch6ZBQjhkohRgFWkuZCZCTJT9TE3RqSD0NleSCXaw7rQYOaQ5EZBaOPSMZAiZAAimIG55YMiC1gxEX1hPnXBp1P6hMYX0savPnYxnxsR2mXW57XZBgEH7ESlZCX6020aqIcT5ib3I3LXiVboS36TwKwanOMgen5a0mWd4DvZCjWyhwJ6e9i0qbop7zgZAAtQzZB3T1lVS6ULNPca7MJsZBoSqi91REZCtcbFZARYEzTZCi5MrZB7a0ZB98nJaMSnZAAUUgTEkinAIhSE0PUIXJz8PKAZDZD",
    )
    PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "1187573034444323")
    VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "12345")
    GRAPH_API_VERSION = os.getenv("GRAPH_API_VERSION", "v23.0")

    # Database
    DATABASE = os.getenv("DATABASE", "chatbot.db")

    # Groq API (free-text answers)
    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY",
        "",
    )
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")