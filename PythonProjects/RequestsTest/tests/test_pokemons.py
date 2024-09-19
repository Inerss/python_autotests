import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'f447dbc91314b404a273855fbff73437'
HEADER = {'Content-Type' : 'Application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5315'

def test_pokemon_status_code():
    response = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Ипман'