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
    
def get_member_info(id):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members WHERE id=?", (id,))
    member_data = cursor.fetchone()
    connection.close()
    return member_data

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
    if 8 <= len(username) <= 12:
        if username[0].isalpha() or username[0] == '_':
            for char in username[1:]:
                if not (char.isalnum() or char in "_'."):
                    return False
            return True
    return False

def is_valid_password(password):
    if 12 <= len(password) <= 30:
        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        special_chars = set("~!@#$%&_-+=`|\\(){}[]:;'<>,.?/")
        has_special = any(char in special_chars for char in password)

        if has_lowercase and has_uppercase and has_digit and has_special:
            return True

    return False

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

def id_exists(id):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM members WHERE id = ?", (id,))
    user_count = cursor.fetchone()[0]

    if user_count > 0:
        connection.close()
        return True
    
    connection.close
    return False

def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password

def is_valid_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) == 7:
        return True
    
    else:
        return False
    
def is_valid_name(name):
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'") 
    if (len(name) <= 20 and name != ""):   
        return all(character in allowed_characters for character in name)
    
    else:
        return False
    
def is_valid_age(age):
    if (age.isdigit() and int(age) > 0):
        return True
    
    else:
        return False

def is_valid_email(email):
    try:
        first_part, last_part = email.split('@')
        
        if ("@" in email and "." in last_part and first_part != "" and last_part != "" and not " " in first_part and not " " in last_part):
            return True
        
        else:
            return False
        
    except ValueError:
        return False

def is_valid_weight(weight):
    try:
        weight = float(weight)
        if (weight > 0):
            return True
        
        else:
            return False
    
    except ValueError:
        return False
    
def is_valid_gender(gender):
    genders = ["Male", "Female", "Other"]
    
    if gender in genders:
        return True
    else:
        return False
    
def is_valid_street_name(street_name):
    if (street_name.isalpha()):
        return True
    
    else:
        return False
    
def is_valid_house_number(house_number):
    if (house_number.isdigit() and int(house_number) > 0):
        return True

    else:
        return False

def is_valid_zip_code(zip_code):
    digits = zip_code[:4]
    letters = zip_code[4:]

    if (len(zip_code) == 6 and digits.isdigit() and letters.isalpha() and letters.isupper()):
        return True
    
    else:
        return False
    
def is_valid_city(city):
    cities = ["Almere", "Amsterdam", "Breda", "Den Haag", "Eindhoven", "Groningen", "Nijmegen", "Rotterdam", "Tilburg", "Utrecht"]

    if city in cities:
        return True
    else:
        return False
    
def is_valid_address(street_name, house_number, zip_code, city):
    if (street_name != "" and house_number != "" and zip_code != "" and city != ""):
        return True
    
    else:
        return False