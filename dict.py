import requests
import sys

apiRequest = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

searchWord = sys.argv[1]
file = open("key.txt")
for line in file:
    apiKey = line
file.close()

apiRequest += (searchWord + "?key=" + apiKey)

req = requests.get(apiRequest)
jsonData = req.json()

shortDef = jsonData[0]['shortdef'][0]
descriptor = jsonData[0]['fl']


print('<' + searchWord + ' (' + descriptor + ')>\n'+ shortDef)
