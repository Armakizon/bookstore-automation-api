import requests
from helpers.generate_token import generate_token

def add_book_to_user(token, isbn):
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

    assert response.status_code == 201 or response.status_code == 400, f"Expected status 201 but got {response.status_code}"

    resp_json = response.json()
    assert "books" in resp_json, "Response missing 'books' key, Make sure book wasnt on the booklist before "

    # Confirm the returned books list contains the ISBN you added
    isbns = [book["isbn"] for book in resp_json["books"]]
    assert isbn in isbns, f"ISBN {isbn} not found in response books"

    return response

token = generate_token()
isbn = "9781449325862"

add_book_to_user(token, isbn)
