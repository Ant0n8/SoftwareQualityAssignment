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
        self.registration_date = datetime.date.today().strftime("%d-%m-%Y")

    def list_users():
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE role != 'SuperAdmin'")
        users = cursor.fetchall()
        connection.close()
        
        print(f"{' '.ljust(5)} {'Username'.ljust(15)} {'Role'.ljust(15)} {'Firstname'.ljust(15)} {'Lastname'.ljust(15)} {'Registration Date'}\n")
        count = 0
        for user in users:
            count += 1
            print(f"{str(count).ljust(5)} {user[0].ljust(15)} {user[3].ljust(15)} {user[4].ljust(15)} {user[5].ljust(15)} {user[6]}")
        
        print()
        print("Total Users: " + str(count))

    def add_user(user):
        hashed_password = Authentication.hash_password(user.password, user.salt)

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password, salt, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (user.username, hashed_password, user.salt, user.role, user.first_name, user.last_name, user.registration_date))
        connection.commit()
        connection.close()

    def modify_user_info(username, first_name, last_name):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET first_name=?, last_name=? WHERE username=?", 
                       (first_name, last_name, username))
        connection.commit()
        connection.close()

    def delete_user(username):
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