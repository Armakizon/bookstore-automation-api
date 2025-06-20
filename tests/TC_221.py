import requests

def test_generate_token():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": "validusername123",
        "password": "Validpassword123!"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200  # Successful response
    json_response = response.json()

    # Assert the token key exists and is not empty
    assert "token" in json_response
    assert json_response["token"] != ""

    # Optional: print the token for debugging
    print("Generated token:", json_response["token"])
