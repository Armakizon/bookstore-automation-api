import requests

def test_get_books():
    response = requests.get("https://demoqa.com/BookStore/v1/Books")
    assert response.status_code == 200
    assert "books" in response.json()
    print("API check passed! Got", len(response.json()["books"]), "books.")
