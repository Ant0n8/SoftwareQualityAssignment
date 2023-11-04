import datetime
import os
import sqlite3
import Authentication
import Encryption
from SystemAdmin import SystemAdmin

class SuperAdmin(SystemAdmin):
    def __init__(self):
        self.username = "super_admin"
        self.password = "Admin_123!"
        self.salt = os.urandom(16).hex()
        self.role = "SuperAdmin"
        self.first_name = "Super"
        self.last_name = "Admin"
        self.registration_date = datetime.date.today().strftime("%d-%m-%Y")

    def add_super_admin(self):
        if (not Authentication.username_exists(self.username)):
            hashed_password = Authentication.hash_password(self.password, self.salt)

            encrypted_username = Encryption.encrypt_data(Encryption.get_public_key(), self.username.encode('utf-8'))
            encrypted_role = Encryption.encrypt_data(Encryption.get_public_key(), self.role.encode('utf-8'))
            encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), self.first_name.encode('utf-8'))
            encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), self.last_name.encode('utf-8'))
            encrypted_registration_date = Encryption.encrypt_data(Encryption.get_public_key(), self.registration_date.encode('utf-8'))

            connection = sqlite3.connect("FitnessPlus.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, salt, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (encrypted_username, hashed_password, self.salt, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date))
            connection.commit()
            connection.close()