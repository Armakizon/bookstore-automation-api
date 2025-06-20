import requests

USERNAME = "validusername123"
PASSWORD = "Validpassword123!"

def delete_user(user_id, token):
    url = f"https://demoqa.com/Account/v1/User/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.delete(url, headers=headers)
    print("Delete user status:", resp.status_code, resp.text)
    return resp.status_code == 204

def generate_token(username, password):
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers)
    print("Generate token status:", resp.status_code, resp.text)
    if resp.status_code != 200:
        return None
    return resp.json().get("token")

def create_user(username, password):
    url = "https://demoqa.com/Account/v1/User"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers)
    print("Create user status:", resp.status_code, resp.text)
    if resp.status_code in (200, 201):
        try:
            data = resp.json()
            return data.get("userID")
        except Exception:
            print("Failed to parse create user response JSON.")
            return None
    return None

def main():
    # Try to generate token and delete user (optional)
    token = generate_token(USERNAME, PASSWORD)
    if token:
        print("Existing token found, trying to get userId to delete user...")
        user_id = None
        # You could add a function to get userId here if needed
        # but since /User endpoint doesn't return JSON, skipping delete

    # Create user and get userId from response
    user_id = create_user(USERNAME, PASSWORD)
    if not user_id:
        print("User creation failed or user already exists.")
    else:
        print("User ID from creation:", user_id)

    # Generate token for newly created user
    token = generate_token(USERNAME, PASSWORD)
    if token:
        print("Generated token:", token)
    else:
        print("Failed to generate token.")

if __name__ == "__main__":
    main()
