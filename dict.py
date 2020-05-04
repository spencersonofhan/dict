import requests
import sys
import pdb

apiRequest = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
words = 1
flag = ""

# Check for flag arguments
try:
    if sys.argv[1].startswith('-'):
        searchWord = sys.argv[2]
        flag = sys.argv[1]
    else:
        searchWord = sys.argv[1]
except IndexError:
    print("Error: Please enter a word to search for")
    sys.exit(0)


with open('key.txt') as f:
    apiKey = f.readline().strip()

apiRequest += (searchWord + "?key=" + apiKey)

try:    
    req = requests.get(apiRequest)
except requests.exceptions.RequestException as e: # Check if json was succesfully retrieved
    print("Something went wrong, fix connection and try again")
    sys.exit(0)

# JSON data
jsonData = req.json()

# Prints all the homographs
if flag == "-a":
    words = len(jsonData)

for i in range(words):
    try:
        shortDef = jsonData[i]['shortdef'][0]
        descriptor = jsonData[i]['fl']
    except TypeError as e:
        print("Word does not exist | typo")
        sys.exit(0)
    print("-" * 100)
    print('<' + searchWord + ' (' + descriptor + ')>\n'+ shortDef)
print("-" * 100)
