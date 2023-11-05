import SharedInterface


def trainer_screen(username, password, salt, first_name, last_name, registration_date):
    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Trainer Menu")
        print("--------------------------------------------------")
        print("[1] Profile")
        print("[2] Update Own Password")
        print()
        print("[3] Add Member")
        print("[4] Modify Member")
        print("[5] Search Member")
        print()
        print("[0] Logout")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")
        
        if (choice == "1"):
            SharedInterface.profile_screen(first_name, last_name, registration_date)
        
        elif (choice == "2"):
            SharedInterface.update_own_password_screen(username, password, salt)

        elif (choice == "3"):
            SharedInterface.add_member_screen(username)

        elif (choice == "4"):
            SharedInterface.modify_member_screen(username)

        elif (choice == "5"):
            SharedInterface.search_member_screen()

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")