"""
database.py

Database for CE WhatsApp Chatbot
"""

import sqlite3

DATABASE_NAME = "chatbot.db"


def initialize_database():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # User State Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_state(
        user_id TEXT PRIMARY KEY,
        state TEXT NOT NULL
    )
    """)

    # Chatbot Knowledge Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chatbot_data(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        category TEXT NOT NULL,

        subcategory TEXT NOT NULL,

        response TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()


def save_state(user_id, state):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO user_state(user_id,state)
    VALUES(?,?)
    """, (user_id, state))

    conn.commit()
    conn.close()


def get_state(user_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT state
    FROM user_state
    WHERE user_id=?
    """, (user_id,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "MAIN_MENU"


def insert_data(category, subcategory, response):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chatbot_data(category,subcategory,response)
    VALUES(?,?,?)
    """, (category, subcategory, response))

    conn.commit()
    conn.close()


def get_data(category, subcategory):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT response
    FROM chatbot_data
    WHERE category=? AND subcategory=?
    """, (category, subcategory))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "Information not available."