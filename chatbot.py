from responses import *
from state_manager import get_state, set_state


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
            return FACULTY_INFO

        elif message == "3":
            return DEPARTMENT_INFO

        elif message == "4":
            return FACILITIES_INFO

        elif message == "5":
            return CONTACT_INFO

        else:
            return UNKNOWN_MESSAGE


    # ---------------- ADMISSION MENU ----------------

    elif state == "ADMISSION_MENU":

        if message == "1":
            return ELIGIBILITY_INFO

        elif message == "2":
            return FEES_INFO

        elif message == "3":
            set_state(user_id, "DOCUMENT_MENU")
            return DOCUMENT_MENU

        elif message == "4":
            return ADMISSION_PROCESS

        elif message == "0":
            set_state(user_id, "MAIN_MENU")
            return MAIN_MENU

        else:
            return UNKNOWN_MESSAGE


    # ---------------- DOCUMENT MENU ----------------

    elif state == "DOCUMENT_MENU":

        if message == "1":
            return GENERAL_DOCUMENTS

        elif message == "2":
            return EWS_DOCUMENTS

        elif message == "3":
            return OBC_DOCUMENTS

        elif message == "4":
            return SEBC_DOCUMENTS

        elif message == "5":
            return SC_DOCUMENTS

        elif message == "6":
            return ST_DOCUMENTS

        elif message == "0":
            set_state(user_id, "ADMISSION_MENU")
            return ADMISSION_MENU

        else:
            return UNKNOWN_MESSAGE


    return UNKNOWN_MESSAGE