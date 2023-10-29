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
        print()
        print("[0] Back")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")
        
        if (choice == "1"):
            add_member_screen()
        
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
        print("[1] First Name: ")
        print("[2] Last Name: ")
        print("[3] Age: ")
        print("[4] Gender: ")
        print("[5] Weight: ")
        print("[6] Address: ")
        print("[7] Email: ")
        print("[8] Phone Number: ")
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