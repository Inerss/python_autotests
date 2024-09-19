import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'f447dbc91314b404a273855fbff73437'
HEADER = {'Content-Type' : 'Application/json', 'trainer_token' : TOKEN}
body_creation = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_creation)
print(response_create.text)

message = response_create.json()['message']
print(message)

body_change = {
    "pokemon_id": "35039",
    "name": "OLOLOSHA",
    "photo_id": 6
}
response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_addPoke = {
    "pokemon_id": "72711"
}

response_change = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_addPoke)
print(response_change.text)