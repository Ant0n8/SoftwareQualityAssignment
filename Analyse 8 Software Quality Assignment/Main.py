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


# SuperAdmin.list_users()
# SuperAdmin.list_members()
Database.create_database()
super_admin = SuperAdmin()
super_admin.add_super_admin()

loop = True
while (loop):
    current_user = None
    username, password = SharedInterface.login_screen()
    login_succesful = Authentication.login(username, password)
    role = Authentication.role_check(username)

    if (login_succesful):
        current_user = Authentication.get_user_info(username)
        current_user_role = current_user[0]
        
        if (role[0] == "Trainer"):
            TrainerInterface.trainer_screen()

        elif (role[0] == "SystemAdmin"):
            SystemAdminInterface.system_admin_screen()

        elif (role[0] == "SuperAdmin"):
            current_user = SuperAdmin()
            SuperAdminInterface.super_admin_screen()

    else:
        print("Invalid username or password")
        input("Press 'Enter' to continue")