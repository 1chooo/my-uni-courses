import requests

def login_to_website(username, password):
    url = 'http://140.115.59.7:12005/'  # Replace 'http://example.com/' with the actual URL

    # Form data to be sent
    payload = {
        'username': username,
        'password': password,
        'submit': 'ログイン'
    }

    try:
        # Sending a POST request with the form data
        response = requests.post(url, data=payload)

        # Checking the response status code
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f"Login failed. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual credentials
    login_to_website('your_username', 'your_password')
