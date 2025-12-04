import logging
import os 

LOG_FILE_PATH = 'logs/app.log'  

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message):
    logging.info(message)


def validate_amount(amount):
    try:
        value = float(amount)
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        return value
    except ValueError as e:
        log(f"Invalid amount: {amount}. Error: {e}")
        raise