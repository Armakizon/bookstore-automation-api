import requests

def test_get_books():
    response = requests.get("https://demoqa.com/BookStore/v1/Book?ISBN=9781449325862")
    assert response.status_code == 200
    response_json = response.json() 
    assert "Git Pocket Guide" in response_json["title"]
    assert "version control system" in response_json["description"]
    print("No books found")
