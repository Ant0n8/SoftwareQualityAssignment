import datetime
import os
import sqlite3
import Authentication
import Encryption
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

    def delete_member(id):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM members")
        member_data = cursor.fetchall()

        if (member_data):
            for data in member_data:
                encrypted_id = data[0]

                decrypted_id = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_id).decode('utf-8')
                
                if (decrypted_id == id):
                    cursor.execute("DELETE FROM members WHERE id=?", (encrypted_id,))
                    connection.commit()

        connection.close()

    def list_users():
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username, role, first_name, last_name, registration_date FROM users WHERE role != 'SuperAdmin'")
        users = cursor.fetchall()
        connection.close()
        
        print(f"{' '.ljust(5)} {'Username'.ljust(15)} {'Role'.ljust(15)} {'Firstname'.ljust(15)} {'Lastname'.ljust(15)} {'Registration Date'}\n")
        count = 0
        for user in users:
            count += 1

            encrypted_username, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date = user
        
            decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')
            decrypted_role = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_role).decode('utf-8')
            decrypted_first_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_first_name).decode('utf-8')
            decrypted_last_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_last_name).decode('utf-8')
            decrypted_registration_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_registration_date).decode('utf-8')

            print(f"{str(count).ljust(5)} {decrypted_username.ljust(15)} {decrypted_role.ljust(15)} {decrypted_first_name.ljust(15)} {decrypted_last_name.ljust(15)} {decrypted_registration_date}")
        
        print()
        print("Total Users: " + str(count))

    def add_user(user):
        hashed_password = Authentication.hash_password(user.password, user.salt)

        encrypted_username = Encryption.encrypt_data(Encryption.get_public_key(), user.username.encode('utf-8'))
        encrypted_role = Encryption.encrypt_data(Encryption.get_public_key(), user.role.encode('utf-8'))
        encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), user.first_name.encode('utf-8'))
        encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), user.last_name.encode('utf-8'))
        encrypted_registration_date = Encryption.encrypt_data(Encryption.get_public_key(), user.registration_date.encode('utf-8'))

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password, salt, role, first_name, last_name, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (encrypted_username, hashed_password, user.salt, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_registration_date))
        connection.commit()
        connection.close()

    def modify_user_info(username, first_name, last_name):
        encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), first_name.encode('utf-8'))
        encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), last_name.encode('utf-8'))

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users")
        user_data = cursor.fetchall()

        if (user_data):
            for data in user_data:
                encrypted_username = data[0]

                decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')
                
                if (decrypted_username == username):
                    cursor.execute("UPDATE users SET first_name=?, last_name=? WHERE username=?", 
                                (encrypted_first_name, encrypted_last_name, encrypted_username))
                    connection.commit()
        
        connection.close()

    def delete_user(username):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users")
        user_data = cursor.fetchall()

        if (user_data):
            for data in user_data:
                encrypted_username = data[0]

                decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')
                
                if (decrypted_username == username):
                    cursor.execute("DELETE FROM users WHERE username=?", (encrypted_username,))
                    connection.commit()

        connection.close()

    # def backup_system(self):
    #     # Implement logic to create a backup of the system.

    # def restore_backup(self, backup_file):
    #     # Implement logic to restore a system backup.

    # def view_logs(self):
    #     # Implement logic to view system logs.