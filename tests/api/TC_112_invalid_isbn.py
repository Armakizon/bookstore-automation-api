import requests

def test_get_books():
    response = requests.get("https://demoqa.com/BookStore/v1/Book?ISBN=1234567")
    assert response.status_code == 400
    print("No books found")
