import datetime
import os
import sqlite3
import Authentication
from Trainer import Trainer

class SystemAdmin(Trainer):
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.salt = os.urandom(16).hex()
        self.role = "SystemAdmin"
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = datetime.date.today()

    def list_users():
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        connection.close()
        
        number = 1
        for user in users:
            print("[" + str(number) + "]" + " " + str(user))
            number += 1

    def add_trainer(trainer):
        hashed_password = Authentication.hash_password(trainer.password, trainer.salt)

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password, salt, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (trainer.username, hashed_password, trainer.salt, trainer.role, trainer.first_name, trainer.last_name, trainer.registration_date))
        connection.commit()
        connection.close()

    def modify_trainer_info(username, updated_info):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET first_name=?, last_name=? WHERE username=?", 
                       (updated_info.first_name, updated_info.last_name, username))
        connection.commit()
        connection.close()

    def delete_trainer(username):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        connection.commit()
        connection.close()

    def reset_trainer_password(new_password, username):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        connection.commit()
        connection.close()

    # def backup_system(self):
    #     # Implement logic to create a backup of the system.

    # def restore_backup(self, backup_file):
    #     # Implement logic to restore a system backup.

    # def view_logs(self):
    #     # Implement logic to view system logs.

    def delete_member(id):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM members WHERE id=?", (id,))
        connection.commit()
        connection.close()