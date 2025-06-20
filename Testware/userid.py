import requests

def get_user_id():
    username = "validusername123"
    password = "Validpassword123!"

    # Step 1: Generate token
    token_url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {"Content-Type": "application/json"}

    token_response = requests.post(token_url, json=payload, headers=headers)
    if token_response.status_code != 200:
        print("Failed to generate token:", token_response.json())
        return None

    token = token_response.json().get("token")
    if not token:
        print("Token not found in response.")
        return None

    # Step 2: Get user info using token
    user_info_url = f"https://demoqa.com/Account/v1/User/{username}"
    headers["Authorization"] = f"Bearer {token}"

    user_response = requests.get(user_info_url, headers=headers)
    if user_response.status_code != 200:
        print("Failed to get user info:", user_response.json())
        return None

    user_data = user_response.json()
    user_id = user_data.get("userId")
    if not user_id:
        print("UserId not found in user data.")
        return None

    return user_id

# Run the function and print the userId
user_id = get_user_id()
if user_id:
    print("User ID:", user_id)
else:
    print("Could not retrieve user ID.")
