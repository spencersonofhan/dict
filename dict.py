import requests
import sys

apiRequest = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

searchWord = sys.argv[1]
file = open("key.txt")
for line in file:
    apiKey = line
file.close()

apiRequest += (searchWord + "?key=" + apiKey)

r = requests.get(apiRequest)
print(r.text)