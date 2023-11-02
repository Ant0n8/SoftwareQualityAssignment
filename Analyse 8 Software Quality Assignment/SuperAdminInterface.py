import Authentication
import SharedInterface
from Member import Member
from Trainer import Trainer
from SystemAdmin import SystemAdmin
from SuperAdmin import SuperAdmin


def super_admin_screen():
    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Super Admin Menu")
        print("--------------------------------------------------")
        print("[1] Add Member")
        print("[2] Modify Member")
        print("[3] Delete Member")
        print("[4] List Members")
        print()
        print("[5] Add User")
        print("[6] Modify User")
        print("[7] Delete User")
        print("[8] List Users")
        print()
        print("[9] Search Member")
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")
        
        if (choice == "1"):
            add_member_screen()
        
        elif (choice == "2"):
            modify_member_screen()

        elif (choice == "3"):
            delete_member_screen()

        elif (choice == "4"):
            list_members_screen()

        elif (choice == "5"):
            add_user_screen()

        elif (choice == "6"):
            modify_user_screen()

        elif (choice == "7"):
            delete_user_screen()
        
        elif (choice == "8"):
            list_users_screen()

        elif (choice == "9"):
            search_member_screen()

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def add_member_screen():
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
        SharedInterface.clear_console()
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
            first_name = input("First Name: ")
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "2"):
            last_name = input("Last Name: ") 
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
                SharedInterface.clear_console()
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
                print("Bad input incident logged")
                input()
                loop = False
        
        elif (choice == "5"):
            weight = input("Weight: ")
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
                SharedInterface.clear_console()
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
                    street_name = input("Street Name: ")
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
                    zip_code = input("Zip Code (DDDDXX): ")
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
            email = input("Email: ")
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

def add_user_screen():
    username = ""
    password = ""
    first_name = ""
    last_name = ""
   
    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Add User")
        print("--------------------------------------------------")
        print("[1] Username: " + username)
        print("[2] Password: " + password)
        print("[3] First Name: " + first_name)
        print("[4] Last Name: " + last_name)
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
            first_name = input("First Name: ")
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "4"):
            last_name = input("Last Name: ") 
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""
      
        elif (choice == "9"):
            if (first_name != "" and last_name != ""):
                confirm = input("Type 'trainer' to add Trainer or 'systemadmin' to add SystemAdmin or press 'Enter' to cancel: ")
                if (confirm == "trainer"):
                    new_trainer = Trainer(username, password, first_name, last_name)
                    SuperAdmin.add_user(new_trainer)
                    print("Trainer added succesfully")
                    input("Press 'Enter' to continue")
                    loop = False

                elif (confirm == "systemadmin"):
                    new_system_admin = SystemAdmin(username, password, first_name, last_name)
                    SuperAdmin.add_user(new_system_admin)
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

def list_members_screen():
    loop = True
    while (loop):
        print("List Members")
        print("--------------------------------------------------")
        SuperAdmin.list_members()
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

def list_users_screen():
    loop = True
    while (loop):
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

def delete_member_screen():
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
        SharedInterface.clear_console()
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

def delete_user_screen():
    username = ""
    role = ""
    first_name = ""
    last_name = ""
    registration_date = ""

    loop = True
    while (loop):
        SharedInterface.clear_console()
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
            if (Authentication.get_user_info(username) != None):
                user = Authentication.get_user_info(username)
                username = user[0]
                role = user[3]
                first_name = user[4]
                last_name = user[5]
                registration_date = user[6]

            else:
                print("Invalid Username")
                input("Press 'Enter' to continue")

        elif (choice == "9"):
            if (username != ""):
                confirm = input("Type 'delete' to delete user or press 'Enter' to cancel: ")
                if (confirm == "delete"):
                    SuperAdmin.delete_user(username)
                    print("User deleted succesfully")
                    input("Press 'Enter' to continue")
                    loop = False

                else:
                    print("User not deleted")
                    input("Press 'Enter' to continue")
            
            else:
                print("Invalid username")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def modify_member_screen():
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
        SharedInterface.clear_console()
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

        elif (choice == "2"):
            first_name = input("First Name: ")
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "3"):
            last_name = input("Last Name: ") 
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
                SharedInterface.clear_console()
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
                print("Bad input incident logged")
                input()
                loop = False
        
        elif (choice == "6"):
            weight = input("Weight: ")
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
                SharedInterface.clear_console()
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
                    street_name = input("Street Name: ")
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
                    zip_code = input("Zip Code (DDDDXX): ")
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
            email = input("Email: ")
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

def modify_user_screen():
    username = ""
    role = ""
    first_name = ""
    last_name = ""
    registration_date = ""

    loop = True
    while (loop):
        SharedInterface.clear_console()
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
            if (Authentication.get_user_info(username) != None):
                user = Authentication.get_user_info(username)
                username = user[0]
                role = user[3]
                first_name = user[4]
                last_name = user[5]
                registration_date = user[6]

            else:
                print("Invalid Username")
                input("Press 'Enter' to continue")

        elif (choice == "2"):
            first_name = input("First Name: ")
            if (not Authentication.is_valid_name(first_name)):
                print("Invalid first name")
                input("Press 'Enter' to continue")
                first_name = ""

        elif (choice == "3"):
            last_name = input("Last Name: ") 
            if (not Authentication.is_valid_name(last_name)):
                print("Invalid last name")
                input("Press 'Enter' to continue")
                last_name = ""

        elif (choice == "9"):
            if (first_name != "" and last_name != ""):
                confirm = input("Type 'modify' to modify user or press 'Enter' to cancel: ")
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
        SharedInterface.clear_console()
        print("Search Member")
        print("--------------------------------------------------")
        print("[1] Search Key")
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")

        if (choice == "1"):
            search_key = input("Search Key: ")
            SuperAdmin.search_member(search_key)
            input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")