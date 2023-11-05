import os
import shutil
import zipfile


def backup():
    backup_path = os.getcwd()
    db_file = "FitnessPlus.db"
    log_file = "activity.log"
    database_backup_file = os.path.join(backup_path, "database_backup.db")
    log_backup_file = os.path.join(backup_path, "logs_backup.txt")

    shutil.copy(db_file, database_backup_file)
    shutil.copy(log_file, log_backup_file)

    count = 1
    while True:
        backup_filename = f"backup{count}.zip"
        if not os.path.exists(os.path.join(backup_path, backup_filename)):
            break
        count += 1

    with zipfile.ZipFile(os.path.join(backup_path, backup_filename), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(database_backup_file, "database_backup.db")
        zipf.write(log_backup_file, "logs_backup.txt")

    os.remove(database_backup_file)
    os.remove(log_backup_file)

def restore():
    backup_path = os.getcwd()
    db_file = "FitnessPlus.db"
    log_file = "activity.log"

    latest_backup_number = 0
    latest_backup_filename = ""
    
    for filename in os.listdir(backup_path):
        if filename.startswith("backup") and filename.endswith(".zip"):
            try:
                count = int(filename[len("backup"):-len(".zip")])
                if count > latest_backup_number:
                    latest_backup_number = count
                    latest_backup_filename = filename
            except ValueError:
                pass

    backup_file = os.path.join(backup_path, latest_backup_filename)

    with zipfile.ZipFile(backup_file, 'r') as zipf:
        zipf.extract("database_backup.db", backup_path)
        zipf.extract("logs_backup.txt", backup_path) 

    shutil.copy(os.path.join(backup_path, "database_backup.db"), db_file)
    shutil.copy(os.path.join(backup_path, "logs_backup.txt"), log_file)