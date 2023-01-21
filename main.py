import requests

token = 'f6f2e3f257da0d4940dcd7101bff17fc'

response = requests.post('https://pokemonbattle.me:5000/trainers/reg', json = {
    "trainer_token": token,
    "email": 'kaloshinm@inbox.ru',
    "password": "Iloveqa1"

}, headers = {'Content-Type': 'application/json'})

print(response.text)

response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', json = {
    "trainer_token": token,
}, headers = {'Content-Type': 'application/json'}
)
print(response_confirm.status_code)

create_pokemon = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    "name": "Бульбазаврapi",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}, headers = {'trainer_token': token}
)

print(create_pokemon.text) # 3191

put_pokemon = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    "pokemon_id" : 3191,
    "name": "Бульбазавр123",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}, headers = {'trainer_token': token}
)
print(put_pokemon.text)

add_to_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id" : "3191",
}, headers = {'trainer_token': token}
)
print(add_to_pokeball.text)
