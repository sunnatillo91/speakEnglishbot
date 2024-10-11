import requests
import json
from pprint import pprint as print
from jsonExtract import jsonExtract

app_id = "9949aa54"
app_key = "526f6635fa6ecc4b9306f52508e0efe2"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f" {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    # will return audiofile
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return  output

if __name__ == "__main__":
    from pprint import pprint as print
    # print(getDefinitions('Great Britain'))
    print(getDefinitions('apple'))

