"""
state_manager.py

Stores the current menu/state of each user.
"""

# Dictionary to store user states
user_states = {}


def get_state(user_id):
    """
    Returns the current state of the user.
    If the user is new, return MAIN_MENU.
    """
    return user_states.get(user_id, "MAIN_MENU")


def set_state(user_id, state):
    """
    Saves the current state of the user.
    """
    user_states[user_id] = state


def reset_state(user_id):
    """
    Resets the user back to the Main Menu.
    """
    user_states[user_id] = "MAIN_MENU"