def validate_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, but got {response.status_code}"


def validate_json_key(response, key):
    data = response.json()
    assert key in data, f"Key '{key}' not found in response"


def validate_json_value(response, key, expected_value):
    data = response.json()
    assert data.get(key) == expected_value, \
        f"Expected {key}={expected_value}, but got {data.get(key)}"
    

def validate_response_time(response, max_time_ms):
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time < max_time_ms, (
        f"Response time {response_time} ms exceeded limit of {max_time_ms} ms"
    )