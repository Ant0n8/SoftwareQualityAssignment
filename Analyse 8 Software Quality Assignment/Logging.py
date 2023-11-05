import logging
import sqlite3
import Encryption
from datetime import datetime

def add_log(username, activity, additional_info, suspicious):
    log_number = get_log_count() + 1
    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().time().strftime("%H:%M:%S")

    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()

    encrypted_number = Encryption.encrypt_data(Encryption.get_public_key(), str(log_number).encode('utf-8'))
    encrypted_date = Encryption.encrypt_data(Encryption.get_public_key(), str(current_date).encode('utf-8'))
    encrypted_time = Encryption.encrypt_data(Encryption.get_public_key(), str(current_time).encode('utf-8'))
    encrypted_username = Encryption.encrypt_data(Encryption.get_public_key(), str(username).encode('utf-8'))
    encrypted_activity = Encryption.encrypt_data(Encryption.get_public_key(), str(activity).encode('utf-8'))
    encrypted_additional_info = Encryption.encrypt_data(Encryption.get_public_key(), str(additional_info).encode('utf-8'))
    encrypted_suspicious = Encryption.encrypt_data(Encryption.get_public_key(), str(suspicious).encode('utf-8'))

    cursor.execute("INSERT INTO logs (number, date, time, username, activity, additional_info, suspicious) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (encrypted_number, encrypted_date, encrypted_time, encrypted_username, encrypted_activity, encrypted_additional_info, encrypted_suspicious))
    connection.commit()
    connection.close()

def get_logs():
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logs")
    logs_data = cursor.fetchall()
    connection.close()

    for data in logs_data:
        encrypted_number, encrypted_date, encrypted_time, encrypted_username, encrypted_activity, encrypted_additional_info, encrypted_suspicious = data
    
        decrypted_number = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_number).decode('utf-8')
        decrypted_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_date).decode('utf-8')[:15]
        decrypted_time = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_time).decode('utf-8')[:15]
        decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')[:15]
        decrypted_activity = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_activity).decode('utf-8')[:25]
        decrypted_additional_info = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_additional_info).decode('utf-8')[:30]
        decrypted_suspicious = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_suspicious).decode('utf-8')

        print(f"{decrypted_number.ljust(5)} {decrypted_date.ljust(15)} {decrypted_time.ljust(15)} {decrypted_username.ljust(15)} {decrypted_activity.ljust(25)} {decrypted_additional_info.ljust(30)} {decrypted_suspicious}")

def get_log_count():
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logs")
    logs_data = cursor.fetchall()
    connection.close()

    count = 0
    for data in logs_data:
        count += 1

    return count

def get_alert():
    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT suspicious FROM logs")
    logs_data = cursor.fetchall()
    connection.close()

    for data in logs_data:
        encrypted_suspicious = data[0]
    
        decrypted_suspicious = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_suspicious).decode('utf-8')

        if (decrypted_suspicious == "Yes"):
            return True
        
    return False