import sqlite3

def create_database():
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            role TEXT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender TEXT,
            weight REAL,
            address TEXT,
            email TEXT,
            phone_number TEXT,
            registration_date TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            salt TEXT,
            role TEXT,
            first_name TEXT,
            last_name TEXT,
            registration_date TEXT
        )
    ''')

    connection.commit()
    connection.close()