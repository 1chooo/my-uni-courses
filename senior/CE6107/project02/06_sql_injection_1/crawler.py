import requests

def save_web_content_to_html(url, file_name):
    try:
        # Sending a GET request
        response = requests.get(url)

        # Checking the response status code
        if response.status_code == 200:
            # Saving the web content to a file
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Successfully saved the web content as {file_name}")
        else:
            print(f"Failed to access the URL, Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url_to_scrape = 'http://140.115.59.7:12005/'
    file_to_save = 'index.html'

    save_web_content_to_html(url_to_scrape, file_to_save)
