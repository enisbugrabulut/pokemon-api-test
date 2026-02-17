import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(pokemon_name):
    url = base_url + "pokemon/" + pokemon_name
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Pokemon ID : {pokemon_data["id"]}")
        print(f"Pokemon Name : {pokemon_data["name"]}")
        print(f"Pokemon Order : {pokemon_data["order"]}")
        print(f"Pokemon Height : {pokemon_data["height"]}")
        print(f"Pokemon Weight : {pokemon_data["weight"]}")
    else:
        print(f"Failed to retrieve pokemon {pokemon_name}. Status code: {response.status_code}")

pokemonName = input("Enter pokemon name: ")
get_pokemon(pokemonName)