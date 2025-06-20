import requests

def test_generate_token():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": "Invaliduser",
        "password": "Invaliduser"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200  # OK response

    response_json = response.json()
    assert response_json.get("token") is None  # token is null in JSON
