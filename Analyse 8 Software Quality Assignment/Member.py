import random
import datetime

class Member:
    def __init__(self, first_name, last_name, age, gender, weight, address, email, phone_number):
        self.registration_date = datetime.date.today().strftime("%d-%m-%Y")
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

    def generate_id():
        current_year = datetime.now().year % 100
        random_digits = [str(random.randint(0, 9)) for _ in range(7)]

        digits = [int(digit) for digit in str(current_year) + "".join(random_digits)]
        checksum = sum(digits) % 10

        id = f"{current_year}{''.join(random_digits)}{checksum}"

        return id