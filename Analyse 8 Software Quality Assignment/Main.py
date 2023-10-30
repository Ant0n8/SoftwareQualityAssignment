import Database
import Authentication
import SharedInterface
import TrainerInterface
import SystemAdminInterface
import SuperAdminInterface
from Member import Member
from Trainer import Trainer  
from SystemAdmin import SystemAdmin
from SuperAdmin import SuperAdmin


Database.create_database()
super_admin = SuperAdmin()
super_admin.add_super_admin()

loop = True
while (loop):
    current_user = None
    username, password = SharedInterface.login_screen()
    login_succesful = Authentication.login(username, password)
    role = Authentication.role_check(username)

    if (username == "None" and password == "None"):
        loop = False

    elif (login_succesful):
        current_user = Authentication.get_user_info(username)
        current_user_username = current_user[0]
        current_user_password = current_user[1]
        current_user_salt = current_user[2]
        current_user_role = current_user[3]
        current_user_first_name = current_user[4]
        current_user_last_name = current_user[5]
        current_user_registration_date = current_user[6]
        
        if (current_user_role == "Trainer"):
            TrainerInterface.trainer_screen()

        elif (current_user_role == "SystemAdmin"):
            SystemAdminInterface.system_admin_screen()

        elif (current_user_role == "SuperAdmin"):
            current_user = SuperAdmin()
            SuperAdminInterface.super_admin_screen()

    else:
        print("Invalid username or password")
        input("Press 'Enter' to continue")