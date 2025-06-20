import requests

USERNAME = "validusername123"
PASSWORD = "Validpassword123!"

def generate_token(username, password):
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers)
    print("Generate token status:", resp.status_code, resp.text)
    if resp.status_code == 200 and resp.json().get("token"):
        return resp.json().get("token")
    return None

def create_user(username, password):
    url = "https://demoqa.com/Account/v1/User"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers)
    print("Create user status:", resp.status_code, resp.text)
    if resp.status_code in (200, 201):
        try:
            return resp.json().get("userID")
        except Exception:
            print("Failed to parse create user response JSON.")
    return None

def main():
    print("\n=== Create user ===")
    user_id = create_user(USERNAME, PASSWORD)
    if user_id:
        print("User ID:", user_id)
    else:
        print("User already exists or creation failed.")

    print("\n=== Generate token ===")
    token = generate_token(USERNAME, PASSWORD)
    if token:
        print("Token:", token)
    else:
        print("Failed to generate token.")

if __name__ == "__main__":
    main()
