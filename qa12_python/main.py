import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '664f24b5cd4840cea318171f834d941e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "JSON MAMOA",
    "photo": "https://dolnikov.ru/pokemons/albums/088.png"
}

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": f"{pokemon_id}",
    "name": "PUTPUT"
}

response_change = requests.patch(url= f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_poketball = {
    "pokemon_id": f"{pokemon_id}"
}

response_poketball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_poketball)
print(response_poketball.text)