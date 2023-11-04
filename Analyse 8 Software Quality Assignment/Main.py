import Database
import Authentication
import SharedInterface
import TrainerInterface
import SystemAdminInterface
import SuperAdminInterface
import Encryption
import Logging
from SuperAdmin import SuperAdmin


Encryption.generate_keys()
Database.create_database()
super_admin = SuperAdmin()
super_admin.add_super_admin()
logger = Logging.setup_logging()

loop = True
while (loop):
    current_user = None
    username, password = SharedInterface.login_screen()
    login_succesful = Authentication.login(username, password)
    role = Authentication.role_check(username)

    if (login_succesful):
        current_user = Authentication.get_user_info(username)
        current_user_username = current_user[0]
        current_user_password = current_user[1]
        current_user_salt = current_user[2]
        current_user_role = current_user[3]
        current_user_first_name = current_user[4]
        current_user_last_name = current_user[5]
        current_user_registration_date = current_user[6]

        # Log succesful login attempt
        logger.info(f"{current_user_username} Logged in No")

        if (current_user_role == "Trainer"):
            TrainerInterface.trainer_screen(current_user_username, current_user_password, current_user_salt, current_user_first_name, current_user_last_name, current_user_registration_date)

        elif (current_user_role == "SystemAdmin"):
            SystemAdminInterface.system_admin_screen(current_user_username, current_user_password, current_user_salt, current_user_role, current_user_first_name, current_user_last_name, current_user_registration_date)

        elif (current_user_role == "SuperAdmin"):
            SuperAdminInterface.super_admin_screen(current_user_password, current_user_salt, current_user_role)

    else:
        print("Invalid username or password")
        input("Press 'Enter' to continue")