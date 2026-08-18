import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ce_chatbot_secret_key")

    # WhatsApp Cloud API
    ACCESS_TOKEN = os.getenv(
        "WHATSAPP_ACCESS_TOKEN",
        "EAAahMmMvp5kBSMCVM6pzSYCwZCm9I31DWmQh5otSFPsZC8KBjRZCgoCPGByflkHBcLkZBhbmikmGTe4HYl7eEjwRqAgnsi3t0516rVJYtbsmHKd49kQFL1TRUS6ZCoCb80i7fgrmTzXo6bXEKQUYzZAXE1CJQ9ZA8dT5UW3l1ZBAU2lpN00X2seAneR3tTa9F90cN6dlK28AFA5KSePDZC8SHbeokAxO55ZAvYCUYFrcwGNTQ3HwTj1u0pf93U6FTZCEqpicJhxZC18j8eMQoeFbN1mn3Yx0ZAtyQ86BEWJmYagZDZD",
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