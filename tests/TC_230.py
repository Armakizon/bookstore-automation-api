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

    json_response = response.json()

    return json_response["token"]

def add_book_to_user(token,isbn):
    url = "https://demoqa.com/BookStore/v1/Books"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "userId": "f12a52b9-43c5-499a-8124-d3145f0113c9",
        "collectionOfIsbns": [{"isbn": isbn}]
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    return response

token = test_generate_token()
isbn = "9781449325862"

add_book_to_user(token, isbn)
