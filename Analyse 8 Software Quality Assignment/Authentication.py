import hashlib
import sqlite3
import Encryption


def login(username, password):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username, password, salt FROM users")
    user_data = cursor.fetchall()
    connection.close()

    if(user_data):
        for data in user_data:
            encrypted_username, stored_password, stored_salt = data

            decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')

            if (decrypted_username == username):
                hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt.encode('utf-8'), 100000)

                if (hashed_password == stored_password):
                    return True
                else:
                    return False

    return False

    
def get_member_info(id):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members")
    member_data = cursor.fetchall()
    connection.close()

    if (member_data):
        for data in member_data:
            encrypted_registration_date, encrypted_id, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number = data

            decrypted_id = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_id.encode('utf-8'))
            
            if (decrypted_id == id):
                decrypted_registration_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_registration_date.encode('utf-8'))
                decrypted_role = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_role.encode('utf-8'))
                decrypted_first_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_first_name.encode('utf-8'))
                decrypted_last_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_last_name.encode('utf-8'))
                decrypted_age = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_age.encode('utf-8'))
                decrypted_gender = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_gender.encode('utf-8'))
                decrypted_weight = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_weight.encode('utf-8'))
                decrypted_address = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_address.encode('utf-8'))
                decrypted_email = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_email.encode('utf-8'))
                decrypted_phone_number = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_phone_number.encode('utf-8'))

                member_data = (decrypted_registration_date, decrypted_id, decrypted_role, decrypted_first_name, decrypted_last_name, decrypted_age, decrypted_gender, decrypted_weight, decrypted_address, decrypted_email, decrypted_phone_number)
                break

    return member_data

def get_user_info(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    user_data = cursor.fetchall()
    connection.close()

    if (user_data):
        for data in user_data:
            encrypted_username, password, salt, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date = data
            
            decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')

            if (decrypted_username == username):
                decrypted_role = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_role).decode('utf-8')
                decrypted_first_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_first_name).decode('utf-8')
                decrypted_last_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_last_name).decode('utf-8')
                decrypted_registration_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_registration_date).decode('utf-8')

                user_data = (decrypted_username, password, salt, decrypted_role, decrypted_first_name, decrypted_last_name, decrypted_registration_date)
                break

    return user_data

def role_check(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username, role FROM users")
    user_data = cursor.fetchall()
    connection.close()
    
    if (user_data):
        for data in user_data:
            encrypted_username, encrypted_role = data

            decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')

            if (decrypted_username == username):
                decrypted_role = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_role).decode('utf-8')
                user_data = decrypted_role
                break

    return user_data

def username_exists(username):
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM users")
    user_data = cursor.fetchall()
    connection.close

    if (user_data):
        for data in user_data:
            encrypted_username = data

            decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')

            if (decrypted_username == username):
                return True
            break
    
    return False

def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password

def is_valid_username(username):
    if 8 <= len(username) <= 12 and (username[0].isalpha() or username[0] == "_") and all(char.isalnum() or char in "_'." for char in username[1:]):
        return True
    
    else:
        return False

def is_valid_password(password):
    if (12 <= len(password) <= 30):
        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        special_chars = set("~!@#$%&_-+=`|\\(){}[]:;'<>,.?/")
        has_special = any(char in special_chars for char in password)

        if has_lowercase and has_uppercase and has_digit and has_special:
            return True
        
        else:
            return False
        
    else:
        return False

def is_valid_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) == 8:
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