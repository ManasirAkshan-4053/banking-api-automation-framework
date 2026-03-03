# schemas/transaction_schema.py

transaction_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "amount": {"type": "number"},
        "type": {"type": "string"},
        "description": {"type": "string"},
        "user_id": {"type": "number"}
    },
    "required": ["id", "amount", "type", "description", "user_id"]
}