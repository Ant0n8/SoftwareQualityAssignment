import datetime
import hashlib
import os
import sqlite3
import Authentication
from SystemAdmin import SystemAdmin

class SuperAdmin(SystemAdmin):
    def __init__(self):
        self.username = "super_admin"
        self.password = "Admin_123!"
        self.salt = os.urandom(16).hex()
        self.role = "SuperAdmin"
        self.first_name = "Super"
        self.last_name = "Admin"
        self.registration_date = datetime.date.today()

    def add_super_admin(self):
        if (not Authentication.username_exists(self.username)):
            password = self.password
            hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt.encode('utf-8'), 100000)

            connection = sqlite3.connect("FitnessPlus.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, salt, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (self.username, hashed_password, self.salt, self.role, self.first_name, self.last_name, self.registration_date))
            connection.commit()
            connection.close()

    def list_members():
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members")
        users = cursor.fetchall()
        connection.close()
        
        for user in users:
            print(user)