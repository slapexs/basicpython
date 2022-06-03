from unittest import result
import requests

def getfact():
    url = 'https://www.catfact.ninja/fact'
    response = requests.get(url)
    result = response.json()
    return result["fact"]


def geturlcatfact(times):
    list_facts = []
    for i in range(times):    
        url = 'https://www.catfact.ninja/fact'
        res = requests.get(url)
        result = res.json()
        list_facts.append(result["fact"])
    return list_facts
