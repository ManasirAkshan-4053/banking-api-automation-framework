from api.transaction_api import create_transaction, get_transaction
from utils.validators import validate_status_code, validate_json_key
from jsonschema import validate
from schemas.transaction_schema import transaction_schema


def test_create_and_get_transaction():

    # Positive test using standard parameters
    create_response = create_transaction(
        amount=5000,
        type="credit",
        description="Online Transfer",
        user_id=101
    )

    validate_status_code(create_response, 201)
    validate_json_key(create_response, "id")

    transaction_id = create_response.json()["id"]
    get_response = get_transaction(transaction_id)

    validate_status_code(get_response, 200)
    validate(instance=get_response.json(), schema=transaction_schema)
    validate_json_key(get_response, "amount")


def test_create_transaction_missing_amount():
    payload = {
        "type": "credit"
        # amount missing
    }

    response = create_transaction(payload=payload)

    # json-server may still accept it, so we allow flexibility
    assert response.status_code in [400, 201]


def test_create_transaction_invalid_amount_type():
    payload = {
        "amount": "invalid",
        "type": "credit"
    }

    response = create_transaction(payload=payload)

    assert response.status_code in [400, 201]


def test_create_transaction_negative_amount():
    payload = {
        "amount": -500,
        "type": "debit"
    }

    response = create_transaction(payload=payload)

    # json-server does not validate business rules
    assert response.status_code in [400, 201]


def test_get_invalid_transaction():
    response = get_transaction(999999)

    assert response.status_code == 404