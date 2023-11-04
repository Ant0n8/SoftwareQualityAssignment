import datetime
import os
import sqlite3
import Encryption
from Member import Member

class Trainer(Member):
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.salt = os.urandom(16).hex()
        self.role = "Trainer"
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = datetime.date.today().strftime("%d-%m-%Y")

    def update_password(username, new_password):
        encrypted_new_password = Encryption.encrypt_data(Encryption.get_public_key(), new_password)

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET password=? WHERE username=?", (encrypted_new_password, username))
        connection.commit()
        connection.close()

    def add_member(member):
        encrypted_registration_date = Encryption.encrypt_data(Encryption.get_public_key(), member.registration_date.encode('utf-8'))
        encrypted_id = Encryption.encrypt_data(Encryption.get_public_key(), member.id.encode('utf-8'))
        encrypted_role = Encryption.encrypt_data(Encryption.get_public_key(), member.role.encode('utf-8'))
        encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), member.first_name.encode('utf-8'))
        encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), member.last_name.encode('utf-8'))
        encrypted_age = Encryption.encrypt_data(Encryption.get_public_key(), member.age.encode('utf-8'))
        encrypted_gender = Encryption.encrypt_data(Encryption.get_public_key(), member.gender.encode('utf-8'))
        encrypted_weight = Encryption.encrypt_data(Encryption.get_public_key(), member.weight.encode('utf-8'))
        encrypted_address = Encryption.encrypt_data(Encryption.get_public_key(), member.address.encode('utf-8'))
        encrypted_email = Encryption.encrypt_data(Encryption.get_public_key(), member.email.encode('utf-8'))
        encrypted_phone_number = Encryption.encrypt_data(Encryption.get_public_key(), member.phone_number.encode('utf-8'))

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO members (registration_date, id, role, first_name, last_name, age, gender, weight, address, email, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (encrypted_registration_date, encrypted_id, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number))
        connection.commit()
        connection.close()

    def modify_member_info(id, first_name, last_name, age, gender, weight, address, email, phone_number):
        encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), first_name.encode('utf-8'))
        encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), last_name.encode('utf-8'))
        encrypted_age = Encryption.encrypt_data(Encryption.get_public_key(), age.encode('utf-8'))
        encrypted_gender = Encryption.encrypt_data(Encryption.get_public_key(), gender.encode('utf-8'))
        encrypted_weight = Encryption.encrypt_data(Encryption.get_public_key(), weight.encode('utf-8'))
        encrypted_address = Encryption.encrypt_data(Encryption.get_public_key(), address.encode('utf-8'))
        encrypted_email = Encryption.encrypt_data(Encryption.get_public_key(), email.encode('utf-8'))
        encrypted_phone_number = Encryption.encrypt_data(Encryption.get_public_key(), phone_number.encode('utf-8'))

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE members SET first_name=?, last_name=?, age=?, gender=?, weight=?, address=?, email=?, phone_number=? WHERE id=?",
            (encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number, id))
        connection.commit()
        connection.close()

    def search_member(search_key):
        if (search_key == ""):
            print("Results: 0")
            return

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members WHERE id LIKE ? OR first_name LIKE ? OR last_name LIKE ? OR address LIKE ? OR email LIKE ? OR phone_number LIKE ?",
            (f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%'))
        members = cursor.fetchall()
        connection.close()
        
        print(f"{'ID'.ljust(15)} {'Firstname'.ljust(15)} {'LastName'.ljust(15)} {'Age'.ljust(15)} {'Gender'.ljust(15)} {'Weight'.ljust(15)} {'Address'.ljust(30)} {'Email'.ljust(25)} {'Phone Number'.ljust(15)} {'Registration Date'}\n")
        number = 0
        for member in members:
            number += 1

            encrypted_registration_date, encrypted_id, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number = member

            decrypted_registration_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_registration_date.encode('utf-8'))
            decrypted_id = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_id.encode('utf-8'))
            decrypted_first_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_first_name.encode('utf-8'))
            decrypted_last_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_last_name.encode('utf-8'))
            decrypted_age = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_age.encode('utf-8'))
            decrypted_gender = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_gender.encode('utf-8'))
            decrypted_weight = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_weight.encode('utf-8'))
            decrypted_address = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_address.encode('utf-8'))
            decrypted_email = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_email.encode('utf-8'))
            decrypted_phone_number = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_phone_number.encode('utf-8'))

            print(f"{str(decrypted_id).ljust(15)} {decrypted_first_name.ljust(15)} {decrypted_last_name.ljust(15)} {str(decrypted_age).ljust(15)} {decrypted_gender.ljust(15)} {str(decrypted_weight).ljust(15)} {decrypted_address.ljust(30)} {decrypted_email.ljust(25)} {decrypted_phone_number.ljust(15)} {decrypted_registration_date}")

        print("\nResults: " + str(number))