# This script is used to fetch data from the PokeAPI using Ray
# Copilot helped generate some of the code based on the initial comments and function names

# Import Modules/Dependencies
import csv
import ray
import requests
import time

# Initialize Ray
ray.init()

# Define a function to fetch data from the PokeAPI
@ray.remote
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Extract relevant details
        pokemon_id = data.get("id")
        name = data.get("name")
        height = data.get("height")
        weight = data.get("weight")
        base_experience = data.get("base_experience")
        sprite_url = data["sprites"]["front_default"]

        print(f'Fetching data for Pokemon: {name} (ID: {pokemon_id})')

        return {
            "ID": pokemon_id,
            "Name": name,
            "Height": height,
            "Weight": weight,
            "Base Experience": base_experience,
            "Sprite URL": sprite_url,
        }
    
    except requests.RequestException as e:
        # Return the URL and error status if the request fails
        return {"ID": None, "Name": None, "Height": None, "Weight": None, "Base Experience": None, "Sprite URL": None, "error": str(e)}
    
def main():
    # URLs for all 1024 Pokémon
    urls = [f'https://pokeapi.co/api/v2/pokemon/{i}' for i in range(1, 1025)]

    # Open CSV and write header
    with open("pokemon_data_ray.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Height", "Weight", "Base Experience", "Sprite URL"])

        # Start timing
        start_time = time.time()

        # Distribute tasks to Ray
        futures = [fetch_data.remote(url) for url in urls]

        # Gather results from all tasks
        results = ray.get(futures)

        # Write results to CSV
        for result in results:
            if result["ID"]:  # Ensure the result is valid
                writer.writerow([
                    result["ID"],
                    result["Name"],
                    result["Height"],
                    result["Weight"],
                    result["Base Experience"],
                    result["Sprite URL"],
                ])

        # Calculate and print total execution time
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()