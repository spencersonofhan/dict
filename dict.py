import requests
import sys
import pdb

apiRequest = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

searchWord = sys.argv[1]
file = open("key.txt")
for line in file:
    apiKey = line
file.close()

apiRequest += (searchWord + "?key=" + apiKey)

try:    
    req = requests.get(apiRequest)
except requests.exceptions.RequestException as e: # Check if json was succesfully retrieved
    print("Something went wrong, attempt to fix connection and try again")
    sys.exit(0)

jsonData = req.json()

try:
    shortDef = jsonData[0]['shortdef'][0]
    descriptor = jsonData[0]['fl']
except TypeError as e:
    print("Word does not exist | typo")
    sys.exit(0)

print('<' + searchWord + ' (' + descriptor + ')>\n'+ shortDef)
