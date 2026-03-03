# schemas/transaction_schema.py

transaction_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "userId": {"type": "number"}
    },
    "required": ["id", "title", "description", "userId"]
}