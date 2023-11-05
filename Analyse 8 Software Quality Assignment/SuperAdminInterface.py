import SharedInterface
import Logging

def super_admin_screen(username, role):
    alert_message = ""
    alert = Logging.get_alert()
    if (alert):
        alert_message = "(Suspicious Activity)"

    loop = True
    while (loop):
        SharedInterface.clear_console()
        print("Super Admin Menu")
        print("--------------------------------------------------")
        print("[1] Add Member")
        print("[2] Modify Member")
        print("[3] Delete Member")
        print("[4] Search Member")
        print()
        print("[5] Add User")
        print("[6] Modify User")
        print("[7] Delete User")
        print("[8] List Users")
        print("[9] Update User Password")
        print()
        print("[10] Check Logs " + alert_message)
        print("[11] Backup")
        print()
        print("[0] Logout")
        print("--------------------------------------------------")
        choice = input("Select an option: ")
        print("--------------------------------------------------")
        
        if (choice == "1"):
            SharedInterface.add_member_screen(username)
        
        elif (choice == "2"):
            SharedInterface.modify_member_screen(username)

        elif (choice == "3"):
            SharedInterface.delete_member_screen(username)

        elif (choice == "4"):
            SharedInterface.search_member_screen()

        elif (choice == "5"):
            SharedInterface.add_user_screen(username, role)

        elif (choice == "6"):
            SharedInterface.modify_user_screen(username, role)

        elif (choice == "7"):
            SharedInterface.delete_user_screen(username, role)
        
        elif (choice == "8"):
            SharedInterface.list_users_screen()

        elif (choice == "9"):
            SharedInterface.update_user_password_screen(username, role)

        elif (choice == "10"):
            SharedInterface.logs_screen(role)

        elif (choice == "11"):
            SharedInterface.backup_screen()

        elif (choice == "0"):
            loop = False

        else:
            print("Invalid option")
            input("Press 'Enter' to continue")