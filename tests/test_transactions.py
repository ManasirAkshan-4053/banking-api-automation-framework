from urllib import response

from api.transaction_api import create_transaction, get_transaction
from utils.validators import validate_status_code, validate_json_key
from jsonschema import validate
from schemas.transaction_schema import transaction_schema

def test_create_and_get_transaction():

    create_response = create_transaction(
        "Online Transfer",
        "Credit 5000",
        101
    )

    validate_status_code(create_response, 201)
    validate_json_key(create_response, "id")

    transaction_id = create_response.json()["id"]
    get_response = get_transaction(transaction_id)

    validate_status_code(get_response, 200)
    validate(instance=get_response.json(), schema=transaction_schema)

    validate_status_code(get_response, 200)
    validate_json_key(get_response, "title")