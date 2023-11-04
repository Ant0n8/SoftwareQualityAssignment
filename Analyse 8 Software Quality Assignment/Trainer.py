import datetime
import os
import sqlite3
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
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        connection.commit()
        connection.close()

    def add_member(member):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO members (registration_date, id, role, first_name, last_name, age, gender, weight, address, email, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (member.registration_date, member.id, member.role, member.first_name, member.last_name, member.age, member.gender, member.weight, member.address, member.email, member.phone_number))
        connection.commit()
        connection.close()

    def modify_member_info(id, first_name, last_name, age, gender, weight, address, email, phone_number):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE members SET first_name=?, last_name=?, age=?, gender=?, weight=?, address=?, email=?, phone_number=? WHERE id=?",
            (first_name, last_name, age, gender, weight, address, email, phone_number, id))
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
            print(f"{str(member[0]).ljust(15)} {member[2].ljust(15)} {member[3].ljust(15)} {str(member[4]).ljust(15)} {member[5].ljust(15)} {str(member[6]).ljust(15)} {member[7].ljust(30)} {member[8].ljust(25)} {member[9].ljust(15)} {member[10]}")

        print("\nResults: " + str(number))