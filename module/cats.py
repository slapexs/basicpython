import requests

def getfact():
    url = 'https://www.catfact.ninja/fact'
    response = requests.get(url)
    result = response.json()
    return result["fact"]

