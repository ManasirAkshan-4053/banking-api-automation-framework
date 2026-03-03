import requests
from utils.config import BASE_URL
from utils.logger import get_logger
from utils.config_loader import load_config

config = load_config()
BASE_URL = config["base_url"]

logger = get_logger(__name__)

def create_transaction(amount=None, type=None, description=None, user_id=None, payload=None):

    if payload is None:
        payload = {
            "amount": amount,
            "type": type,
            "description": description,
            "user_id": user_id
        }

    return requests.post(f"{config['base_url']}/transactions", json=payload)

    logger.info(f"Creating transaction: {title}")
    response = requests.post(url, json=payload)

    logger.info(f"Response Status: {response.status_code}")
    return response


def get_transaction(transaction_id):
    url = f"{BASE_URL}/transactions/{transaction_id}"

    logger.info(f"Fetching transaction ID: {transaction_id}")
    response = requests.get(url)

    logger.info(f"Response Status: {response.status_code}")
    return response