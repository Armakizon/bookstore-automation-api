import requests

def generate_token():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": "validusername123",
        "password": "Validpassword123!"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    json_response = response.json()

    return json_response["token"]
