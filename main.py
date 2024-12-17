import requests

def pokemon_data():
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

pokemon_name = input("Enter your pokemon: ")
pokemon_info = pokemon_data()

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

    print("Type:")
    for type_info in pokemon_info["types"]:
        print(f" --> {type_info["type"]["name"]}")

    print("Stats:")
    for stat in pokemon_info["stats"]:
        print(f" --> {stat["stat"]["name"]}: {stat["base_stat"]}")

    print("Abilities:")
    for ability in pokemon_info["abilities"]:
        print(f" --> {ability["ability"]["name"]}")
else:
    print("Failed to retrieve Pokemon information.")
