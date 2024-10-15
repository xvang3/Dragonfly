# This script is used to fetch data from the PokeAPI from a single node (no Ray)
# Copilot helped generate some of the code based on the initial comments and function names

# Import Modules/Dependencies
import csv
import requests
import time

# Define a function to fetch data from the PokeAPI
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from URL: {url}")
        return {"error": str(e)}

# For the sake of this example, we will only fetch data for the first 50 Pokémon
urls = [f'https://pokeapi.co/api/v2/pokemon/{i}' for i in range(1, 51)]

# Open CSV and write header
with open("pokemon_data_single.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Height", "Weight", "Base Experience", "Sprite URL"])

    # Start timing
    start_time = time.time()

    # Fetch data for each Pokémon
    for url in urls:
        data = fetch_data(url)

        if "error" in data:
            continue

        # Extract relevant details
        pokemon_id = data.get("id")
        name = data.get("name")
        height = data.get("height")
        weight = data.get("weight")
        base_experience = data.get("base_experience")
        sprite_url = data["sprites"]["front_default"]

        print(f'Fetching data for Pokemon: {name} (ID: {pokemon_id})')

        # Write data to CSV
        writer.writerow([pokemon_id, name, height, weight, base_experience, sprite_url])

    # End timing
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

print("Data fetching complete!")