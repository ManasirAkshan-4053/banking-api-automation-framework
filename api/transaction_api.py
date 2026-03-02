import requests
from utils.config import BASE_URL
from utils.logger import get_logger

logger = get_logger(__name__)

def create_transaction(title, description, user_id):
    url = f"{BASE_URL}/transactions"

    payload = {
        "title": title,
        "description": description,
        "userId": user_id
    }

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