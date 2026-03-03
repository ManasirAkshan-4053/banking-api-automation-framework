import json
import os

def load_config():
    env = os.getenv("ENV", "dev")
    config_path = f"config/{env}.json"

    print("ENV VALUE:", env)
    print("CONFIG PATH:", os.path.abspath(config_path))

    with open(config_path, "r") as config_file:
        content = config_file.read()
        print("FILE CONTENT:", content)
        return json.loads(content)