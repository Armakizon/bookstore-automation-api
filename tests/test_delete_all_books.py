import requests
from test_generate_token import test_generate_token




def delete_all_books():
    token=test_generate_token()
    url = "https://demoqa.com/BookStore/v1/Books"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"userId": "c200d043-997c-4e94-99cd-2038a80a6f16"}
    response = requests.delete(url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    return response.status_code == 204

delete_all_books()
