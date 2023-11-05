import SharedInterface


def system_admin_screen(username, password, salt, role, first_name, last_name, registration_date):
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
        print("[5] Delete Member")
        print("[6] Search Member")
        print()
        print("[7] Add User")
        print("[8] Modify User")
        print("[9] Delete User")
        print("[10] List Users")
        print("[11] Update User Password")
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
            SharedInterface.add_member_screen()

        elif (choice == "4"):
            SharedInterface.modify_member_screen()

        elif (choice == "5"):
            SharedInterface.delete_member_screen()

        elif (choice == "6"):
            SharedInterface.search_member_screen()

        elif (choice == "7"):
            SharedInterface.add_user_screen(role)

        elif (choice == "8"):
            SharedInterface.modify_user_screen(role)

        elif (choice == "9"):
            SharedInterface.delete_user_screen(role)
        
        elif (choice == "10"):
            SharedInterface.list_users_screen()

        elif (choice == "11"):
            SharedInterface.update_user_password_screen(role)

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")