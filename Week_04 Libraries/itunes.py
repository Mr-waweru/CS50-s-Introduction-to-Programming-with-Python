import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

# Make a http request using python to the server
# Similar to typing the url in a browser and pressing enter 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])


o = response.json()
for result in o["results"]:
    print(result["trackName"])











