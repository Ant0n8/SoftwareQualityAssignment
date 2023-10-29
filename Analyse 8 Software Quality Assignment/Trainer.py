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
        self.registration_date = datetime.date.today()

    def update_password(self, new_password):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, self.username))
        connection.commit()
        connection.close()

    def add_member(member):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO members (registration_date, id, role, first_name, last_name, age, gender, weight, address, email, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (member.registration_date, member.id, member.role, member.first_name, member.last_name, member.age, member.gender, member.weight, member.address, member.email, member.phone_number))
        connection.commit()
        connection.close()

    def modify_member_info(id, updated_info):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE members SET first_name=?, last_name=?, age=?, gender=?, weight=?, address=?, email=?, phone_number=? WHERE id=?",
            (updated_info.first_name, updated_info.last_name, updated_info.age, updated_info.gender, updated_info.weight, updated_info.address, updated_info.email, updated_info.phone_number, id))
        connection.commit()
        connection.close()

    def search_member(search_key):
        connection = sqlite3.connect("FitnessPlus.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members WHERE id LIKE ? OR first_name LIKE ? OR last_name LIKE ? OR address LIKE ? OR email LIKE ? OR phone_number LIKE ?",
            (f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%', f'%{search_key}%'))
        result = cursor.fetchall()
        connection.close()
        return result