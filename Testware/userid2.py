import requests

def get_user_by_username(username, password):
    # Step 1: Generate token
    token_url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {"Content-Type": "application/json"}
    token_response = requests.post(token_url, json=payload, headers=headers)

    if token_response.status_code != 200:
        print("Failed to generate token:", token_response.text)
        return

    token = token_response.json().get("token")
    if not token:
        print("Token not found in response.")
        return

    # Step 2: Get user info by username with proper headers
    user_info_url = f"https://demoqa.com/Account/v1/User/{username}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    user_response = requests.get(user_info_url, headers=headers)

    print("User info response status:", user_response.status_code)
    print("User info response text:", user_response.text)

get_user_by_username("validusername123", "Validpassword123!")
