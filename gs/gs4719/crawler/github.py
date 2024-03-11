import requests

query_string = '''
{
    viewer {
        login
    }
    repository(name: "Python-Community", owner: "NCU-GS4719-Python") {
        discussions(first: 10) {
            edges {
                node {
                    id
                    title
                }
            }
        }
    }
}
'''

api_url = "https://api.github.com/graphql"
github_personal_access_token = ""
response = requests.post(
    api_url, 
    headers={
        "Authorization": f"bearer {github_personal_access_token}"
    }, 
    json={
        'query': query_string
    }
)
print(response.text)

for _ in response.json()['data']['repository']['discussions']['edges']:
    print(_['node']['title'])
