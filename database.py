"""
database.py

Creates and manages the chatbot database.
"""

import sqlite3

DATABASE_NAME = "chatbot.db"


def initialize_database():
    """
    Creates the chatbot database and required tables.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Store user conversation state
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_state (
            user_id TEXT PRIMARY KEY,
            state TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_state(user_id, state):
    """
    Save or update a user's current state.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO user_state(user_id, state)
        VALUES (?, ?)
    """, (user_id, state))

    conn.commit()
    conn.close()


def get_state(user_id):
    """
    Returns the current state of the user.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT state FROM user_state
        WHERE user_id=?
    """, (user_id,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "MAIN_MENU"