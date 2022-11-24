import requests

url = 'https://www.rtvslo.si/iskalnik?q=iskalni%20niz'

def html(link):
    koda = requests.get(url, headers={"User-Agent": "Requests"}).content
    print(koda)

html(url)