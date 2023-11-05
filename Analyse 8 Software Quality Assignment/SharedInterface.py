import os
import Authentication
import Logging
import Backup
from Member import Member
from Trainer import Trainer
from SystemAdmin import SystemAdmin
from SuperAdmin import SuperAdmin


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def login_screen():
    username = ""
    password = ""

    loop = True
    while (loop):
        clear_console()
        print("Sign In")
        print("--------------------------------------------------")
        print("[1] Username: " + username)
        print("[2] Password: " + '*' * len(password))
        print()
        print("[9] Continue")
        print("[0] Exit")
        print("--------------------------------------------------") 
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            username = input("Username: ")

        elif (choice == "2"):
            password = input("Password: ")

        elif (choice == "9"):
            if (username == "" or password == ""):
                print("Username or Password hasn't been filled in.")
                input("Press 'Enter' to try again")
                continue
            return (username, password)
        
        elif (choice == "0"):
            exit()
        
        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def add_member_screen(username):
    first_name = ""
    last_name = ""
    age = ""
    gender = ""
    weight = ""
    address = ""
    email = ""
    phone_number = ""

    loop = True
    while (loop):
        clear_console()
        print("Add Member")
        print("--------------------------------------------------")
        print("[1] First Name: " + first_name)
        print("[2] Last Name: " + last_name)
        print("[3] Age: " + age)
        print("[4] Gender: " + gender)
        print("[5] Weight: " + weight)
        print("[6] Address: " + address)
        print("[7] Email: " + email)
        print("[8] Phone Number: " + phone_number)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            first_name = input("First Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "2"):
            last_name = input("Last Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""

        elif (choice == "3"):
            age = input("Age: ")
            if (not Authentication.is_valid_age(age)):
                print("Invalid age")
                input("Press 'Enter' to continue")
                age = ""
        
        elif (choice == "4"):
            loop_gender = True
            while (loop_gender):
                clear_console()
                print("[1] Male")
                print("[2] Female")
                print("[3] Other")
                print("--------------------------------------------------")
                gender = input("Gender: ")
                if (gender == "1"):
                    gender = "Male"
                    loop_gender = False

                elif (gender == "2"):
                    gender = "Female"
                    loop_gender = False

                elif (gender == "3"):
                    gender = "Other"
                    loop_gender = False

                else:
                    print("Invalid option")
                    input("Press 'Enter' to continue")
            
            if (not Authentication.is_valid_gender(gender)):
                Logging.add_log(username, "Invalid Input", f'Filled in {gender} for the gender field', "Yes")
                print("Bad input incident logged")
                input()
                loop = False
        
        elif (choice == "5"):
            weight = input("Weight (kg): ")
            if (not Authentication.is_valid_weight(weight)):
                print("Invalid weight")
                input("Press 'Enter' to continue")
                weight = ""

        elif (choice == "6"):
            street_name = ""
            house_number = ""
            zip_code = ""
            city = ""

            loop_address = True
            while (loop_address):
                clear_console()
                print("Address")
                print("--------------------------------------------------")
                print("[1] Street Name: " + street_name)
                print("[2] House Number: " + house_number)
                print("[3] Zip Code: " + zip_code)
                print("[4] City: " + city)
                print()
                print("[9] Continue")
                print("[0] Back")
                print("--------------------------------------------------")
                choice_address = input("Select an option: ")
                print("--------------------------------------------------")

                if (choice_address == "1"):
                    street_name = input("Street Name: ").lower().capitalize()
                    if (not Authentication.is_valid_street_name(street_name)):
                        print("Invalid street name")
                        input("Press 'Enter' to continue")
                        street_name = ""

                elif (choice_address == "2"):
                    house_number = input("House Number: ")
                    if (not Authentication.is_valid_house_number(house_number)):
                        print("Invalid house number")
                        input("Press 'Enter' to continue")
                        house_number = ""

                elif (choice_address == "3"):
                    zip_code = input("Zip Code (DDDDXX): ").upper()
                    if (not Authentication.is_valid_zip_code(zip_code)):
                        print("Invalid zip code")
                        input("Press 'Enter' to continue")
                        zip_code = ""
                
                elif (choice_address == "4"):
                    loop_city = True
                    while (loop_city):
                        print("[1] Almere")
                        print("[2] Amsterdam")
                        print("[3] Breda")
                        print("[4] Den Haag")
                        print("[5] Eindhoven")
                        print("[6] Groningen")
                        print("[7] Nijmegen")
                        print("[8] Rotterdam")
                        print("[9] Tilburg")
                        print("[10] Utrecht")
                        print("--------------------------------------------------")
                        city = input("City: ")
                        
                        if (city == "1"):
                            city = "Almere"
                            loop_city = False

                        elif (city == "2"):
                            city = "Amsterdam"
                            loop_city = False

                        elif (city == "3"):
                            city = "Breda"
                            loop_city = False

                        elif (city == "4"):
                            city = "Den Haag"
                            loop_city = False

                        elif (city == "5"):
                            city = "Eindhoven"
                            loop_city = False

                        elif (city == "6"):
                            city = "Groningen"
                            loop_city = False

                        elif (city == "7"):
                            city = "Nijmegen"
                            loop_city = False

                        elif (city == "8"):
                            city = "Rotterdam"
                            loop_city = False

                        elif (city == "9"):
                            city = "Tilburg"
                            loop_city = False

                        elif (city == "10"):
                            city = "Utrecht"
                            loop_city = False

                        else:
                            print("Invalid option")
                            input("Press 'Enter' to continue")

                    if (not Authentication.is_valid_city(city)):
                        Logging.add_log(username, "Invalid Input", f'Filled in {city} for the city field', "Yes")
                        print("Bad input incident logged")
                        input()
                        loop_address = False
                        loop = False

                elif (choice_address == "9"):
                    if (Authentication.is_valid_address(street_name, house_number, zip_code, city)):
                        address = f"{street_name} {house_number}, {zip_code}, {city}"
                        loop_address = False
                    
                    else:
                        print("Invalid address")
                        input("Press 'Enter' to continue")
                        address = ""

                elif (choice_address == "0"):
                    loop_address = False

                else:
                    print("Invalid option")
                    input("Press 'Enter' to continue")

        elif (choice == "7"):
            email = input("Email: ").lower()
            if (not Authentication.is_valid_email(email)):
                print("Invalid email")
                input("Press 'Enter' to continue")
                email = ""

        elif (choice == "8"):
            phone_number = input("Phone Number: +31-6-")
            if (Authentication.is_valid_phone_number(phone_number)):
                phone_number = "+31-6-" + phone_number

            else:
                print("Invalid phone number")
                input("Press 'Enter' to continue")
                phone_number = ""

        elif (choice == "9"):
            if (first_name != "" and last_name != "" and age != "" and gender != "" and weight != "" and address != "" and email != "" and phone_number != ""):
                confirm = input("Type 'yes' to add member or press 'Enter' to cancel: ")
                if (confirm == "yes"):
                    new_member = Member(first_name, last_name, age, gender, weight, address, email, phone_number)
                    SuperAdmin.add_member(new_member)
                    Logging.add_log(username, "New member is created", f'Name: {first_name} {last_name}', "No")
                    print("Member added succesfully")
                    input("Press 'Enter' to continue")
                    break

                else:
                    print("Member not added")
                    input("Press 'Enter' to continue")

            else:
                print("Not all fields have been filled in")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def add_user_screen(current_user_username, current_user_role):
    username = ""
    password = ""
    first_name = ""
    last_name = ""
    role = ""
    role_print = ""

    if (current_user_role == "SystemAdmin"):
        role = "Trainer"
        role_print = "Role: "

    if (current_user_role == "SuperAdmin"):
        role_print = "[5] Role: " + role
   
    loop = True
    while (loop):
        clear_console()
        print("Add User")
        print("--------------------------------------------------")
        print("[1] Username: " + username)
        print("[2] Password: " + password)
        print("[3] First Name: " + first_name)
        print("[4] Last Name: " + last_name)
        print(role_print + role)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            username = input("Username: ")
            if (not Authentication.is_valid_username(username)):
                print("Invalid username")
                input("Press 'Enter' to continue")
                username = ""
            
            elif (Authentication.username_exists(username)):
                print("Username already exists")
                input("Press 'Enter' to continue")
                username = ""

        elif (choice == "2"):
            password = input("Password: ") 
            if (not Authentication.is_valid_password(password)):
                print("Invalid password")
                input("Press 'Enter' to continue")
                password = ""

        elif (choice == "3"):
            first_name = input("First Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "4"):
            last_name = input("Last Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""

        elif (choice == "5" and current_user_role == "SuperAdmin"):
            loop_role = True
            while (loop_role):
                clear_console()
                print("[1] Trainer")
                print("[2] SystemAdmin")
                print("--------------------------------------------------")
                role = input("Role: ")
                if (role == "1"):
                    role = "Trainer"
                    loop_role = False

                elif (role == "2"):
                    role = "SystemAdmin"
                    loop_role = False

                else:
                    print("Invalid option")
                    input("Press 'Enter' to continue")
            
            if (role != "Trainer" and role != "SystemAdmin"):
                Logging.add_log(current_user_username, "Invalid Input", f'Filled in {role} for the role field', "Yes")
                print("Bad input incident logged")
                input()
                loop = False
      
        elif (choice == "9"):
            if (first_name != "" and last_name != ""):
                confirm = input("Type 'yes' to add user or press 'Enter' to cancel: ")
                if (confirm == "yes" and role == "Trainer"):
                    new_trainer = Trainer(username, password, first_name, last_name)
                    SuperAdmin.add_user(new_trainer)
                    Logging.add_log(username, "New trainer is created", f'Username: {username}', "No")
                    print("Trainer added succesfully")
                    input("Press 'Enter' to continue")
                    loop = False

                elif (confirm == "yes" and role == "SystemAdmin"):
                    new_system_admin = SystemAdmin(username, password, first_name, last_name)
                    SuperAdmin.add_user(new_system_admin)
                    Logging.add_log(username, "New admin is created", f'Username: {username}', "No")
                    print("SystemAdmin added succesfully")
                    input("Press 'Enter' to continue")
                    loop = False

                else:
                    print("User not added")
                    input("Press 'Enter' to continue")
        
            else:
                print("Not all fields have been filled in")
                input("Press 'Enter' to continue")
    
        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def list_users_screen():
    loop = True
    while (loop):
        clear_console()
        print("List Users")
        print("--------------------------------------------------")
        SuperAdmin.list_users()
        print("--------------------------------------------------")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "0"):
            loop = False
        
        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def delete_member_screen(username):
    id = ""
    first_name = ""
    last_name = ""
    age = ""
    gender = ""
    weight = ""
    address = ""
    email = ""
    phone_number = ""
    registration_date = ""

    loop = True
    while (loop):
        clear_console()
        print("Delete Member")
        print("--------------------------------------------------")
        print("[1] Search Id")
        print()
        print("Id: " + id)
        print("First Name: " + first_name)
        print("Last Name: " + last_name)
        print("Age: " + age)
        print("Gender: " + gender)
        print("Weight: " + weight)
        print("Address: " + address)
        print("Email: " + email)
        print("Phone Number: " + phone_number)
        print("Registration Date: " + registration_date)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            id = input("Search Id: ")
            if (Authentication.get_member_info(id) != None):
                member = Authentication.get_member_info(id)
                first_name = member[2]
                last_name = member[3]
                age = member[4]
                gender = member[5]
                weight = member[6]
                address = member[7]
                email = member[8]
                phone_number = member[9]
                registration_date = member[10]

            else:
                print("Invalid Id")
                input("Press 'Enter' to continue")

        elif (choice == "9"):
            if (id != ""):
                confirm = input("Type 'delete' to delete member or press 'Enter' to cancel: ")
                if (confirm == "delete"):
                    SuperAdmin.delete_member(id)
                    Logging.add_log(username, "Deleted member", f"member: {id}", "No")
                    print("Member deleted succesfully")
                    input("Press 'Enter' to continue")
                    loop = False

                else:
                    print("Member not deleted")
                    input("Press 'Enter' to continue")
            
            else:
                print("Invalid Id")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def delete_user_screen(current_user_username, current_user_role):
    username = ""
    role = ""
    first_name = ""
    last_name = ""
    registration_date = ""

    loop = True
    while (loop):
        clear_console()
        print("Delete User")
        print("--------------------------------------------------")
        print("[1] Search Username")
        print()
        print("Username: " + username)
        print("Role: " + role)
        print("First Name: " + first_name)
        print("Last Name: " + last_name)
        print("Registration Date: " + registration_date)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            username = input("Search Username: ")
            if (Authentication.username_exists(username)):
                user = Authentication.get_user_info(username)
                username = user[0]
                role = user[3]
                first_name = user[4]
                last_name = user[5]
                registration_date = user[6]

            else:
                print("Invalid Username")
                input("Press 'Enter' to continue")
                username = ""

        elif (choice == "9"):
            if (username != ""):
                confirm = input("Type 'delete' to delete user or press 'Enter' to cancel: ")
                if (current_user_role == "SuperAdmin"):
                    if (confirm == "delete"):
                        Logging.add_log(current_user_username, "Deleted user", f"user: {username}", "No")
                        SuperAdmin.delete_user(username)
                        print("User deleted succesfully")
                        input("Press 'Enter' to continue")
                        loop = False

                    else:
                        print("User not deleted")
                        input("Press 'Enter' to continue")

                elif (current_user_role == "SystemAdmin" and role == "Trainer"):
                    if (confirm == "delete"):
                        SuperAdmin.delete_user(username)
                        Logging.add_log(current_user_username, "Deleted user", f"trainer: {username}", "No")
                        print("User deleted succesfully")
                        input("Press 'Enter' to continue")
                        loop = False

                    else:
                        print("User not deleted")
                        input("Press 'Enter' to continue")

                elif (current_user_role == "SystemAdmin" and role != "Trainer"):
                    Logging.add_log(current_user_username, "Attempted to delete admin", f"admin: {username}", "Yes")
                    print("Access denied insufficient authority level")
                    input("Press 'Enter' to continue")
            
            else:
                print("Invalid username")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def modify_member_screen(username):
    id = ""
    first_name = ""
    last_name = ""
    age = ""
    gender = ""
    weight = ""
    address = ""
    email = ""
    phone_number = ""
    registration_date = ""

    loop = True
    while (loop):
        clear_console()
        print("Modify Member")
        print("--------------------------------------------------")
        print("[1] Search Id")
        print()
        print("Id: " + id)
        print("[2] First Name: " + first_name)
        print("[3] Last Name: " + last_name)
        print("[4] Age: " + age)
        print("[5] Gender: " + gender)
        print("[6] Weight: " + weight)
        print("[7] Address: " + address)
        print("[8] Email: " + email)
        print("[9] Phone Number: " + phone_number)
        print("Registration Date: " + registration_date)
        print()
        print("[10] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            id = input("Search Id: ")
            if (Authentication.get_member_info(id) != None):
                member = Authentication.get_member_info(id)
                first_name = member[2]
                last_name = member[3]
                age = member[4]
                gender = member[5]
                weight = member[6]
                address = member[7]
                email = member[8]
                phone_number = member[9]
                registration_date = member[10]

            else:
                print("Invalid Id")
                input("Press 'Enter' to continue")
                id = ""

        elif (choice == "2"):
            first_name = input("First Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "3"):
            last_name = input("Last Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""

        elif (choice == "4"):
            age = input("Age: ")
            if (not Authentication.is_valid_age(age)):
                print("Invalid age")
                input("Press 'Enter' to continue")
                age = ""
        
        elif (choice == "5"):
            loop_gender = True
            while (loop_gender):
                clear_console()
                print("[1] Male")
                print("[2] Female")
                print("[3] Other")
                print("--------------------------------------------------")
                gender = input("Gender: ")
                if (gender == "1"):
                    gender = "Male"
                    loop_gender = False

                elif (gender == "2"):
                    gender = "Female"
                    loop_gender = False

                elif (gender == "3"):
                    gender = "Other"
                    loop_gender = False

                else:
                    print("Invalid option")
                    input("Press 'Enter' to continue")
            
            if (not Authentication.is_valid_gender(gender)):
                Logging.add_log(username, "Invalid Input", f'Filled in {gender} for the gender field', "Yes")
                print("Bad input incident logged")
                input()
                loop = False
        
        elif (choice == "6"):
            weight = input("Weight (kg): ")
            if (not Authentication.is_valid_weight(weight)):
                print("Invalid weight")
                input("Press 'Enter' to continue")
                weight = ""

        elif (choice == "7"):
            street_name = ""
            house_number = ""
            zip_code = ""
            city = ""

            loop_address = True
            while (loop_address):
                clear_console()
                print("Address")
                print("--------------------------------------------------")
                print("[1] Street Name: " + street_name)
                print("[2] House Number: " + house_number)
                print("[3] Zip Code: " + zip_code)
                print("[4] City: " + city)
                print()
                print("[9] Continue")
                print("[0] Back")
                print("--------------------------------------------------")
                choice_address = input("Select an option: ")
                print("--------------------------------------------------")

                if (choice_address == "1"):
                    street_name = input("Street Name: ").lower().capitalize()
                    if (not Authentication.is_valid_street_name(street_name)):
                        print("Invalid street name")
                        input("Press 'Enter' to continue")
                        street_name = ""

                elif (choice_address == "2"):
                    house_number = input("House Number: ")
                    if (not Authentication.is_valid_house_number(house_number)):
                        print("Invalid house number")
                        input("Press 'Enter' to continue")
                        house_number = ""

                elif (choice_address == "3"):
                    zip_code = input("Zip Code (DDDDXX): ").upper()
                    if (not Authentication.is_valid_zip_code(zip_code)):
                        print("Invalid zip code")
                        input("Press 'Enter' to continue")
                        zip_code = ""
                
                elif (choice_address == "4"):
                    loop_city = True
                    while (loop_city):
                        print("[1] Almere")
                        print("[2] Amsterdam")
                        print("[3] Breda")
                        print("[4] Den Haag")
                        print("[5] Eindhoven")
                        print("[6] Groningen")
                        print("[7] Nijmegen")
                        print("[8] Rotterdam")
                        print("[9] Tilburg")
                        print("[10] Utrecht")
                        print("--------------------------------------------------")
                        city = input("City: ")

                        if (city == "1"):
                            city = "Almere"
                            loop_city = False

                        elif (city == "2"):
                            city = "Amsterdam"
                            loop_city = False

                        elif (city == "3"):
                            city = "Breda"
                            loop_city = False

                        elif (city == "4"):
                            city = "Den Haag"
                            loop_city = False

                        elif (city == "5"):
                            city = "Eindhoven"
                            loop_city = False

                        elif (city == "6"):
                            city = "Groningen"
                            loop_city = False

                        elif (city == "7"):
                            city = "Nijmegen"
                            loop_city = False

                        elif (city == "8"):
                            city = "Rotterdam"
                            loop_city = False

                        elif (city == "9"):
                            city = "Tilburg"
                            loop_city = False

                        elif (city == "10"):
                            city = "Utrecht"
                            loop_city = False

                        else:
                            print("Invalid option")
                            input("Press 'Enter' to continue")

                    if (not Authentication.is_valid_city(city)):
                        Logging.add_log(username, "Invalid Input", f'Filled in {city} for the city field', "Yes")
                        print("Bad input incident logged")
                        input()
                        loop_address = False
                        loop = False

                elif (choice_address == "9"):
                    if (Authentication.is_valid_address(street_name, house_number, zip_code, city)):
                        address = f"{street_name} {house_number}, {zip_code}, {city}"
                        loop_address = False
                    
                    else:
                        print("Invalid address")
                        input("Press 'Enter' to continue")
                        address = ""

                elif (choice_address == "0"):
                    loop_address = False

                else:
                    print("Invalid option")
                    input("Press 'Enter' to continue")

        elif (choice == "8"):
            email = input("Email: ").lower()
            if (not Authentication.is_valid_email(email)):
                print("Invalid email")
                input("Press 'Enter' to continue")
                email = ""

        elif (choice == "9"):
            phone_number = input("Phone Number: +31-6-")
            if (Authentication.is_valid_phone_number(phone_number)):
                phone_number = "+31-6-" + phone_number

            else:
                print("Invalid phone number")
                input("Press 'Enter' to continue")
                phone_number = ""

        elif (choice == "10"):
            if (first_name != "" and last_name != "" and age != "" and gender != "" and weight != "" and address != "" and email != "" and phone_number != ""):
                confirm = input("Type 'modify' to modify member or press 'Enter' to cancel: ")
                if (confirm == "modify"):
                    if (id != ""):
                        SuperAdmin.modify_member_info(id, first_name, last_name, age, gender, weight, address, email, phone_number)
                        print("Member modified succesfully")
                        input("Press 'Enter' to continue")
                        loop = False
                    
                    else:
                        print("Invalid Id")
                        input("Press 'Enter' to continue")

                else:
                    print("Member not modified")
                    input("Press 'Enter' to continue")

            else:
                print("Not all fields have been filled in")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def modify_user_screen(current_user_name, current_user_role):
    username = ""
    role = ""
    first_name = ""
    last_name = ""
    registration_date = ""

    loop = True
    while (loop):
        clear_console()
        print("Modify User")
        print("--------------------------------------------------")
        print("[1] Search Username")
        print()
        print("Username: " + username)
        print("[2] First Name: " + first_name)
        print("[3] Last Name: " + last_name)
        print("Role: " + role)
        print("Registration Date: " + registration_date)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            username = input("Search Username: ")
            if (Authentication.username_exists(username)):
                user = Authentication.get_user_info(username)
                username = user[0]
                role = user[3]
                first_name = user[4]
                last_name = user[5]
                registration_date = user[6]

            else:
                print("Invalid Username")
                input("Press 'Enter' to continue")
                username = ""

        elif (choice == "2"):
            first_name = input("First Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "3"):
            last_name = input("Last Name: ").lower().capitalize()
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""

        elif (choice == "9"):
            if (first_name != "" and last_name != ""):
                confirm = input("Type 'modify' to modify user or press 'Enter' to cancel: ")
                if (current_user_role == "SuperAdmin"):
                    if (confirm == "modify"):
                        if (username != ""):
                            SuperAdmin.modify_user_info(username, first_name, last_name)
                            print("User modified succesfully")
                            input("Press 'Enter' to continue")
                            loop = False
                        
                        else:
                            print("Invalid Username")
                            input("Press 'Enter' to continue")

                    else:
                        print("User not modified")
                        input("Press 'Enter' to continue")

                elif (current_user_role == "SystemAdmin" and role == "Trainer"):
                    if (confirm == "modify"):
                        if (username != ""):
                            SuperAdmin.modify_user_info(username, first_name, last_name)
                            print("User modified succesfully")
                            input("Press 'Enter' to continue")
                            loop = False
                        
                        else:
                            print("Invalid Username")
                            input("Press 'Enter' to continue")

                    else:
                        print("User not modified")
                        input("Press 'Enter' to continue")

                elif (current_user_role == "SystemAdmin" and role != "Trainer"):
                    Logging.add_log(current_user_name, "Unauthorized", f'Tried to modify member ', "Yes")
                    print("Access denied insufficient authority level")
                    input("Press 'Enter' to continue")

            else:
                print("Not all fields have been filled in")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def search_member_screen():
    loop = True
    while (loop):
        clear_console()
        print("Search Member")
        print("--------------------------------------------------")
        print("[1] Search")
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            search_key = input("Search: ")
            SuperAdmin.search_member(search_key)
            input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def profile_screen(first_name, last_name, registration_date):
    loop = True
    while (loop):
        clear_console()
        print("Profile")
        print("--------------------------------------------------")
        print("First Name: " + first_name)
        print("Last Name: " + last_name)
        print("Registration Date: " + registration_date)
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")
        
def update_own_password_screen(username, password, salt):
    new_password = ""

    loop = True
    while (loop):
        clear_console()
        print("Update Own Password")
        print("--------------------------------------------------")
        print("[1] New Password: " + new_password)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            new_password = input("New Password: ")
            if(not Authentication.is_valid_password(new_password)):
                print("Invalid Password")
                input("Press 'Enter' to continue")
                new_password = ""

        elif (choice == "0"):
            loop = False

        elif (choice == "9"):
            confirm = input("Enter current password to update password or press 'Enter' to cancel: ")
            if (Authentication.hash_password(confirm, salt) == password and Authentication.is_valid_password(new_password)):
                SystemAdmin.update_password(username, Authentication.hash_password(new_password, salt))
                print("Password succesfully updated")
                input("Press 'Enter' to continue")
                loop = False

            elif (Authentication.hash_password(confirm, salt) != password and confirm != ""):
                print("Invalid Password")
                input("Press 'Enter' to continue")

            else:
                print("Password not updated")
                input("Press 'Enter' to continue")

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def update_user_password_screen(current_user_username, role):
    username = ""
    new_password = ""

    loop = True
    while (loop):
        clear_console()
        print("Update User Password")
        print("--------------------------------------------------")
        print("[1] Username: " + username)
        print("[2] New Password: " + new_password)
        print()
        print("[9] Continue")
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            username = input("Username: ")
            if (not Authentication.username_exists(username)):
                print("Invalid Username")
                input("Press 'Enter' to continue")
                username = ""

        elif (choice == "2"):
            new_password = input("New Password: ")
            if(not Authentication.is_valid_password(new_password)):
                print("Invalid Password")
                input("Press 'Enter' to continue")
                new_password = ""

        elif (choice == "0"):
            loop = False

        elif (choice == "9"):
            confirm = input("Enter 'yes' to update user password or press 'Enter' to cancel: ")
            if (username != "" and Authentication.username_exists(username) and role == "SuperAdmin"):
                user_info = Authentication.get_user_info(username)
                user_salt = user_info[2]
                if (confirm == "yes" and Authentication.is_valid_password(new_password)):
                    SystemAdmin.update_password(username, Authentication.hash_password(new_password, user_salt))
                    Logging.add_log(current_user_username, "Updated password", f"user: {username}", "No")
                    print("Password succesfully updated")
                    input("Press 'Enter' to continue")
                    loop = False

                elif (confirm == "yes" and not Authentication.is_valid_password(new_password)):
                    print("Invalid Password")
                    input("Press 'Enter' to continue")

                else:
                    print("Password not updated")
                    input("Press 'Enter' to continue")
            
            elif (username != "" and Authentication.username_exists(username) and role == "SystemAdmin"):
                if (Authentication.role_check(username) == "Trainer"):
                    user_info = Authentication.get_user_info(username)
                    user_salt = user_info[2]
                    if (confirm == "yes" and Authentication.is_valid_password(new_password)):
                        SystemAdmin.update_password(username, Authentication.hash_password(new_password, user_salt))
                        print("Password succesfully updated")
                        input("Press 'Enter' to continue")
                        loop = False

                    elif (confirm == "yes" and not Authentication.is_valid_password(new_password)):
                        print("Invalid Password")
                        input("Press 'Enter' to continue")

                    else:
                        print("Password not updated")
                        input("Press 'Enter' to continue")
                
                else:
                    Logging.add_log(current_user_username, "Attempted to update password", f"user: {username}", "Yes")
                    print("Access denied insufficient authority level")
                    input("Press 'Enter' to continue")

            else:
                print("Invalid Username")
                input("Press 'Enter' to continue")
                username = ""

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def logs_screen(role):
    # Check if user is an administrator, if not return
    if role not in ["SuperAdmin", "SystemAdmin"]:
        return

    loop = True
    while(loop):
        clear_console()
        print("Logs")
        print("--------------------------------------------------")
        print(f"{' '.ljust(5)} {'Date'.ljust(15)} {'Time'.ljust(15)} {'Username'.ljust(15)} {'Activity'.ljust(25)} {'Additional Info'.ljust(30)} {'Suspicious'}\n")
        Logging.get_logs()
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "0"):
            break

def backup_screen():
    loop = True
    while (loop):
        clear_console()
        print("Backup")
        print("--------------------------------------------------")
        print("[1] Backup")
        print("[2] Restore")
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            confirm = input("Type 'yes' to create a backup or press 'Enter' to cancel")
            if (confirm == "yes"):
                Backup.backup()
                print("Backup created succesfully")
                input("Press 'Enter' to continue")
            
            else:
                print("Backup not created")
                input("Press 'Enter' to continue")

        elif (choice == "2"):
            selected_backup = Backup.select_backup()

            if (selected_backup != None):
                Backup.restore_backup(selected_backup)
                print("Backup restored succesfully")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False