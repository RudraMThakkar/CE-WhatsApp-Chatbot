from database import initialize_database, insert_data

initialize_database()

# Clear old data (optional during development)
import sqlite3

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM chatbot_data")

conn.commit()
conn.close()

# ---------------- Admission ----------------

insert_data(
    "admission",
    "eligibility",
    "Candidate must have passed 10th Standard from a recognized board and must be eligible through ACPDC."
)

insert_data(
    "admission",
    "fees",
    "Tuition Fee: ₹1500 per year.\n(Government fees may change according to ACPDC rules.)"
)

insert_data(
    "admission",
    "process",
    "Admission is carried out through the ACPDC counselling process."
)

# ---------------- Documents ----------------

insert_data(
    "documents",
    "general",
    "10th Marksheet\nSchool Leaving Certificate\nAadhaar Card\nPassport Size Photos"
)

insert_data(
    "documents",
    "ews",
    "General Documents\n+ Valid EWS Certificate"
)

insert_data(
    "documents",
    "obc",
    "General Documents\n+ Non-Creamy Layer Certificate"
)

insert_data(
    "documents",
    "sebc",
    "General Documents\n+ SEBC Certificate"
)

insert_data(
    "documents",
    "sc",
    "General Documents\n+ SC Certificate"
)

insert_data(
    "documents",
    "st",
    "General Documents\n+ ST Certificate"
)

# ---------------- Faculty ----------------

insert_data(
    "faculty",
    "all",
    "Faculty details will be updated by the department."
)

# ---------------- Department ----------------

insert_data(
    "department",
    "about",
    "Computer Engineering Department provides quality technical education with modern laboratories."
)

# ---------------- Facilities ----------------

insert_data(
    "facilities",
    "labs",
    "Computer Lab\nInternet Facility\nSmart Classroom\nLibrary"
)

# ---------------- Contact ----------------

insert_data(
    "contact",
    "department",
    "Phone: 02766-220419\nEmail: kdp-patan-dte@gujarat.gov.in"
)

print("Database seeded successfully!")