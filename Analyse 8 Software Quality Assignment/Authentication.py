import re
import hashlib
import os
import sqlite3


def login(username, password):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    cursor.execute("SELECT salt, password FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    connection.close()

    if user_data is None:
        return False

    stored_salt, stored_password = user_data
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt.encode('utf-8'), 100000)

    if (hashed_password == stored_password):
        return True
    else:
        return False
    
def get_user_info(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()
    connection.close()
    return user_data

def role_check(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    cursor.execute("SELECT role FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    connection.close()
    return user_data

def is_valid_username(username):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_\'\.]*$', username) and 8 <= len(username) <= 12

def is_valid_password(password):
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%&_\-\+=`|\\(){}[\]:;\'<>,.?/]).{12,30}$', password)

def username_exists(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    user_count = cursor.fetchone()[0]

    if user_count > 0:
        connection.close()
        return True
    
    connection.close
    return False