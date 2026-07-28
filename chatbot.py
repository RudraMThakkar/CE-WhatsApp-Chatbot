from responses import *
from state_manager import get_state, set_state
from database import get_data

def get_response(user_id, user_message):

    message = user_message.strip()

    state = get_state(user_id)

    # ---------------- MAIN MENU ----------------

    if state == "MAIN_MENU":

        if message.lower() in ["hi", "hello", "hey", "menu", "start"]:
            return MAIN_MENU

        elif message == "1":
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

        else:
            return UNKNOWN_MESSAGE


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

        else:
            return UNKNOWN_MESSAGE


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

        else:
            return UNKNOWN_MESSAGE


    return UNKNOWN_MESSAGE