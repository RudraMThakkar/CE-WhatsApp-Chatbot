"""
chatbot.py

- hi / hello / hey / menu / start  → Main Menu
- Menu numbers (1, 2, 3...)        → Database answers
- ANY other message                → Groq AI answer
"""

from responses import *
from state_manager import get_state, set_state
from database import get_data
from ai_helper import get_ai_response


def get_response(user_id, user_message):

    message = user_message.strip()
    lower = message.lower()

    # Always open main menu
    if lower in ["hi", "hello", "hey", "menu", "start"]:
        set_state(user_id, "MAIN_MENU")
        return MAIN_MENU

    state = get_state(user_id)

    # ---------------- MAIN MENU ----------------
    if state == "MAIN_MENU":

        if message == "1":
            set_state(user_id, "ADMISSION_MENU")
            return ADMISSION_MENU

        elif message == "2":
            return get_data("faculty", "all")

        elif message == "3":
            return get_data("department", "about")

        elif message == "4":
            return get_data("facilities", "labs")

        elif message == "5":
            return get_data("contact", "department")

        # Free text → AI (NOT Invalid option)
        return get_ai_response(message)

    # ---------------- ADMISSION MENU ----------------
    elif state == "ADMISSION_MENU":

        if message == "1":
            return get_data("admission", "eligibility")

        elif message == "2":
            return get_data("admission", "fees")

        elif message == "3":
            set_state(user_id, "DOCUMENT_MENU")
            return DOCUMENT_MENU

        elif message == "4":
            return get_data("admission", "process")

        elif message == "0":
            set_state(user_id, "MAIN_MENU")
            return MAIN_MENU

        return get_ai_response(message)

    # ---------------- DOCUMENT MENU ----------------
    elif state == "DOCUMENT_MENU":

        if message == "1":
            return get_data("documents", "general")

        elif message == "2":
            return get_data("documents", "ews")

        elif message == "3":
            return get_data("documents", "obc")

        elif message == "4":
            return get_data("documents", "sebc")

        elif message == "5":
            return get_data("documents", "sc")

        elif message == "6":
            return get_data("documents", "st")

        elif message == "0":
            set_state(user_id, "ADMISSION_MENU")
            return ADMISSION_MENU

        return get_ai_response(message)

    # Fallback → AI
    return get_ai_response(message)