from responses import (
    MAIN_MENU,
    ADMISSION_MENU,
    FEES_INFO,
    CATEGORY_INFO,
    CONTACT_INFO,
    UNKNOWN_MESSAGE
)


def get_response(user_message):
    """
    Returns the chatbot response based on the user's message.
    """

    message = user_message.strip().lower()

    # Main Menu
    if message in ["hi", "hello", "hey", "start", "menu"]:
        return MAIN_MENU

    # Admission Menu
    elif message == "1":
        return ADMISSION_MENU

    # Fees Information
    elif message == "2":
        return FEES_INFO

    # Category Information
    elif message == "3":
        return CATEGORY_INFO

    # Contact Information
    elif message == "4":
        return CONTACT_INFO

    # Go Back
    elif message == "0":
        return MAIN_MENU

    # Invalid Input
    else:
        return UNKNOWN_MESSAGE