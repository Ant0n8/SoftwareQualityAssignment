import logging
import sqlite3
import Encryption

log_counter = 0

def setup_logging(log_file='activity.log', log_level=logging.INFO):
    global log_counter
    
    # Set log counter
    try:
        with open(log_file, 'r') as file:
            # Count the lines in the log file
            log_counter = len(file.readlines()) + 1
    except FileNotFoundError:
        log_counter = 1

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a file handler and set the log file
    file_handler = logging.FileHandler(log_file)

    # Create a formatter and set the log format
    log_format = f'%(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

def get_next_log_number():
    global log_counter
    
    log_number = log_counter
    log_counter += 1

    return log_number

def add_log(number, date, time, username, activity, additional_info, suspicious):
    encrypted_number = Encryption.encrypt_data(Encryption.get_public_key(), str(number).encode('utf-8'))
    encrypted_date = Encryption.encrypt_data(Encryption.get_public_key(), str(date).encode('utf-8'))
    encrypted_time = Encryption.encrypt_data(Encryption.get_public_key(), str(time).encode('utf-8'))
    encrypted_username = Encryption.encrypt_data(Encryption.get_public_key(), str(username).encode('utf-8'))
    encrypted_activity = Encryption.encrypt_data(Encryption.get_public_key(), str(activity).encode('utf-8'))
    encrypted_additional_info = Encryption.encrypt_data(Encryption.get_public_key(), str(additional_info).encode('utf-8'))
    encrypted_suspicious = Encryption.encrypt_data(Encryption.get_public_key(), str(suspicious).encode('utf-8'))

    connection = sqlite3.connect("FitnessPlus.db")
    cursor = connection.cursor()
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
        decrypted_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_date).decode('utf-8')
        decrypted_time = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_time).decode('utf-8')
        decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')
        decrypted_activity = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_activity).decode('utf-8')
        decrypted_additional_info = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_additional_info).decode('utf-8')
        decrypted_suspicious = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_suspicious).decode('utf-8')

        print(f"{decrypted_number.ljust(5)} {decrypted_date.ljust(15)} {decrypted_time.ljust(15)} {decrypted_username.ljust(15)} {decrypted_activity.ljust(15)} {decrypted_additional_info.ljust(25)} {decrypted_suspicious}")