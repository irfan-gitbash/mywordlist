import requests

api_key = '4a8e54ec-8292-4537-8e0d-94cc073c32d4'
word = 'potato'
url =  f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)