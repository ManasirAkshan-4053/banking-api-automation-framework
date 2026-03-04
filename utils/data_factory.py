from faker import Faker
import random

fake = Faker()


def generate_transaction_payload():

    return {
        "amount": random.randint(100, 10000),
        "type": random.choice(["credit", "debit"]),
        "description": fake.sentence(nb_words=4),
        "user_id": random.randint(1, 500)
    }