import random
import datetime

class Member:
    def __init__(self, first_name, last_name, age, gender, weight, address, email, phone_number):
        self.registration_date = datetime.date.today()
        self.id = self.generate_id()
        self.role = "Member"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def generate_id(self):
        registration_year = self.registration_date.year % 100
        id = f"{registration_year}{random.randint(10, 99)}{random.randint(100, 999)}"
        checksum = sum(int(digit) for digit in id) % 10
        id += str(checksum)
        return id