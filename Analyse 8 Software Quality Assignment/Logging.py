import logging

log_counter = 0

def setup_logging(log_file='activity.log', log_level=logging.INFO):
    global log_counter
    
    # Set log counter
    try:
        with open(log_file, 'r') as file:
            # Count the lines in the log file
            log_counter = len(file.readlines()) + 1
    except FileNotFoundError:
        log_counter = 1

    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a file handler and set the log file
    file_handler = logging.FileHandler(log_file)

    # Create a formatter and set the log format
    log_format = f'%(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

def get_next_log_number():
    global log_counter
    
    log_number = log_counter
    log_counter += 1

    return log_number