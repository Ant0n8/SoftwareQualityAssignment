import os
import shutil
import zipfile


def backup():
    backup_path = os.getcwd()
    db_file = "FitnessPlus.db"
    db_backup = "database_backup.db"
    
    database_backup_file = os.path.join(backup_path, db_backup)

    shutil.copy(db_file, database_backup_file)

    count = 1
    while True:
        backup_filename = f"backup{count}.zip"
        if not os.path.exists(os.path.join(backup_path, backup_filename)):
            break
        count += 1

    with zipfile.ZipFile(os.path.join(backup_path, backup_filename), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(database_backup_file, db_backup)

    os.remove(database_backup_file)

def restore_backup(selected_backup):
    backup_path = os.getcwd()
    db_file = "FitnessPlus.db"
    db_backup = "database_backup.db"

    with zipfile.ZipFile(selected_backup, 'r') as zipf:
        zipf.extract(db_backup, backup_path)

    if (os.path.exists(db_file)):
        os.remove(db_file)

    os.rename(os.path.join(backup_path, db_backup), os.path.join(backup_path, db_file))

def select_backup():
    backup_path = os.getcwd()
    backup_files = [filename for filename in os.listdir(backup_path) if filename.startswith("backup") and filename.endswith(".zip")]
    
    if not backup_files:
        print("No backup files found.")
        input("Press 'Enter' to continue")
        return

    count = 0
    for file in backup_files:
        count += 1
        print(f"[{count}] {file}")

    try:
        choice = int(input("Enter the number of the backup file you want to restore or press 'Enter' to cancel: "))
        if 1 <= choice <= len(backup_files):
            return os.path.join(backup_path, backup_files[choice - 1])
        
        else:
            print("Invalid option")
            input("Press 'Enter' to continue")
            return None

    except ValueError:
        print("Invalid option")
        input("Press 'Enter' to continue")
        return None