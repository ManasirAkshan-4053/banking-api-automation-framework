# schemas/transaction_schema.py

transaction_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "amount": {"type": "number"},
        "currency": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["id", "amount", "currency", "status"]
}