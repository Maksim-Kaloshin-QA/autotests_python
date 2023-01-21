import pytest
import requests

def test_get_trainers():
    trainers = requests.get('https://pokemonbattle.me:5000/trainers')
    assert trainers.status_code == 200, "Неожиданный код ответа"

def test_get_my_trainer():
    trainers = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1827'})
    assert trainers.json()['trainer_name'] == 'Maksim'