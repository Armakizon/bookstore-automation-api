import requests
from helpers.generate_token import generate_token

def add_book_to_user(token,isbn):
    url = "https://demoqa.com/BookStore/v1/Books"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "userId": "c200d043-997c-4e94-99cd-2038a80a6f16",
        "collectionOfIsbns": [{"isbn": isbn}]
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    return response

token = generate_token()
isbn = "11111111111"

add_book_to_user(token, isbn)
assert response.status_code == 400
