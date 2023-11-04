import logging

def setup_logging(log_file='activity.log', log_level=logging.INFO):
    # Initialize the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a file handler and set the log file
    file_handler = logging.FileHandler(log_file)

    # Create a formatter and set the log format
    log_format = 'Date Time Username Description of activity Additional Information Suspicious\n%(message)s'
    # log_format = '%(asctime)s %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger