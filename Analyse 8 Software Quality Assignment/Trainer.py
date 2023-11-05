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
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users")
        user_data = cursor.fetchall()

        if (user_data):
            for data in user_data:
                encrypted_username = data[0]
                
                decrypted_username = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_username).decode('utf-8')

                if (decrypted_username == username):
                    cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, encrypted_username))
                    connection.commit()
                    break
                
        connection.close()

    def add_member(member):
        encrypted_id = Encryption.encrypt_data(Encryption.get_public_key(), str(member.id).encode('utf-8'))
        encrypted_role = Encryption.encrypt_data(Encryption.get_public_key(), str(member.role).encode('utf-8'))
        encrypted_first_name = Encryption.encrypt_data(Encryption.get_public_key(), str(member.first_name).encode('utf-8'))
        encrypted_last_name = Encryption.encrypt_data(Encryption.get_public_key(), str(member.last_name).encode('utf-8'))
        encrypted_age = Encryption.encrypt_data(Encryption.get_public_key(), str(member.age).encode('utf-8'))
        encrypted_gender = Encryption.encrypt_data(Encryption.get_public_key(), str(member.gender).encode('utf-8'))
        encrypted_weight = Encryption.encrypt_data(Encryption.get_public_key(), str(member.weight).encode('utf-8'))
        encrypted_address = Encryption.encrypt_data(Encryption.get_public_key(), str(member.address).encode('utf-8'))
        encrypted_email = Encryption.encrypt_data(Encryption.get_public_key(), str(member.email).encode('utf-8'))
        encrypted_phone_number = Encryption.encrypt_data(Encryption.get_public_key(), str(member.phone_number).encode('utf-8'))
        encrypted_registration_date = Encryption.encrypt_data(Encryption.get_public_key(), str(member.registration_date).encode('utf-8'))

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO members (id, role, first_name, last_name, age, gender, weight, address, email, phone_number, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (encrypted_id, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number, encrypted_registration_date))
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
        cursor.execute("SELECT id FROM members")
        member_data = cursor.fetchall()

        if (member_data):
            for data in member_data:
                encrypted_id = data[0]

                decrypted_id = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_id).decode('utf-8')
                
                if (decrypted_id == id):
                    cursor.execute("UPDATE members SET first_name=?, last_name=?, age=?, gender=?, weight=?, address=?, email=?, phone_number=? WHERE id=?",
                        (encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number, encrypted_id))
                    connection.commit()
                    break

        connection.close()

    def search_member(search_key):
        if (search_key == ""):
            print("Results: 0")
            return

        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("Select * FROM members")
        members = cursor.fetchall()
        connection.close()
        
        print(f"{'ID'.ljust(15)} {'Firstname'.ljust(15)} {'LastName'.ljust(15)} {'Age'.ljust(15)} {'Gender'.ljust(15)} {'Weight'.ljust(15)} {'Address'.ljust(30)} {'Email'.ljust(25)} {'Phone Number'.ljust(15)} {'Registration Date'}\n")
        count = 0
        for member in members:
            encrypted_id, encrypted_role, encrypted_first_name, encrypted_last_name, encrypted_age, encrypted_gender, encrypted_weight, encrypted_address, encrypted_email, encrypted_phone_number, encrypted_registration_date = member

            decrypted_id = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_id).decode('utf-8')
            decrypted_first_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_first_name).decode('utf-8')[:15]
            decrypted_last_name = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_last_name).decode('utf-8')[:15]
            decrypted_age = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_age).decode('utf-8')
            decrypted_gender = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_gender).decode('utf-8')
            decrypted_weight = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_weight).decode('utf-8')
            decrypted_address = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_address).decode('utf-8')[:30]
            decrypted_email = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_email).decode('utf-8')[:25]
            decrypted_phone_number = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_phone_number).decode('utf-8')
            decrypted_registration_date = Encryption.decrypt_data(Encryption.get_private_key(), encrypted_registration_date).decode('utf-8')

            if (search_key in decrypted_id or search_key in decrypted_first_name.lower() or search_key in decrypted_last_name.lower() or search_key in decrypted_address.lower() or search_key in decrypted_email or search_key in decrypted_phone_number):
                count += 1
                print(f"{str(decrypted_id).ljust(15)} {decrypted_first_name.ljust(15)} {decrypted_last_name.ljust(15)} {str(decrypted_age).ljust(15)} {decrypted_gender.ljust(15)} {str(decrypted_weight).ljust(15)} {decrypted_address.ljust(30)} {decrypted_email.ljust(25)} {decrypted_phone_number.ljust(15)} {decrypted_registration_date}")

        print("\nResults: " + str(count))