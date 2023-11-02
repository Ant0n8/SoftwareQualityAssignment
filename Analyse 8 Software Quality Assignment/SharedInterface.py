import os

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
        print("[2] Password: " + password)
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
            return (username, password)
        
        elif (choice == "0"):
            exit()
        
        else:
            print("Invalid option")
            input("Press 'Enter' to continue")