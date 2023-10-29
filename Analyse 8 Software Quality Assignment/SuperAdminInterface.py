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
        print("[2] Add Trainer")
        print("[3] Add SystemAdmin")
        print("[4] List Members")
        print("[5] List Users")
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")
        
        if (choice == "1"):
            add_member_screen()
        
        elif (choice == "2"):
            add_trainer_screen()

        elif (choice == "3"):
            add_system_admin_screen()

        elif (choice == "4"):
            list_members_screen()

        elif (choice == "5"):
            list_users_screen()

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

        elif (choice == "2"):
            last_name = input("Last Name: ") 

        elif (choice == "3"):
            age = input("Age: ")
        
        elif (choice == "4"):
            gender = input("Gender: ")
        
        elif (choice == "5"):
            weight = input("Weight: ")

        elif (choice == "6"):
            address = input("Address: ")

        elif (choice == "7"):
            email = input("Email: ")

        elif (choice == "8"):
            phone_number = input("Phone Number: ")

        elif (choice == "9"):
            confirm = input("Type 'yes' to add member or 'Enter' to cancel: ")
            if (confirm == "yes"):
                new_member = Member(first_name, last_name, age, gender, weight, address, email, phone_number)
                SuperAdmin.add_member(new_member)
                print("Member added succesfully")
                input("Press 'Enter' to continue")
                break

            else:
                print("Member not added")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def add_trainer_screen():
    username = ""
    password = ""
    first_name = ""
    last_name = ""
   
    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Add Member")
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
        
        elif (choice == "4"):
            last_name = input("Last Name: ")
      
        elif (choice == "9"):
            confirm = input("Type 'yes' to add trainer or 'Enter' to cancel: ")
            if (confirm == "yes"):
                new_trainer = Trainer(username, password, first_name, last_name)
                SuperAdmin.add_trainer(new_trainer)
                print("Trainer added succesfully")
                input("Press 'Enter' to continue")
                loop = False

            else:
                print("Trainer not added")
                input("Press 'Enter' to continue")

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")

def add_system_admin_screen():
    username = ""
    password = ""
    first_name = ""
    last_name = ""
   
    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Add Member")
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
        
        elif (choice == "4"):
            last_name = input("Last Name: ")
      
        elif (choice == "9"):
            confirm = input("Type 'yes' to add SystemAdmin or 'Enter' to cancel: ")
            if (confirm == "yes"):
                new_system_admin = SystemAdmin(username, password, first_name, last_name)
                SuperAdmin.add_system_admin(new_system_admin)
                print("SystemAdmin added succesfully")
                input("Press 'Enter' to continue")
                loop = False

            else:
                print("SystemAdmin not added")
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