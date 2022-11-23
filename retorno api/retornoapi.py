import requests
import json

def buscar_dados():
    list = []
    request = requests.get("https://brasilapi.com.br/api/banks/v1")
    requestJson = json.loads(request.content)

    for x in range(len(requestJson)):
        del requestJson[x]['ispb']
        del requestJson[x]['fullName']

    list.append(requestJson)
    return list

print(buscar_dados())