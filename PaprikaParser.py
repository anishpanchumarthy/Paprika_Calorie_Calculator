import gzip
import json
import zipfile
from pathlib import Path


def extract_paprika_ingredients(file_path):
    """Extracts and prints the ingredients from a Paprika recipe export file.
    Args: 
        file_path (str): The path to the .paprikarecipes file."""
    path = Path(file_path)
    # Check if the file exists
    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        return

    # Open the main .paprikarecipes Zip archive
    with zipfile.ZipFile(path, "r") as archive:
        # Loop through each item in the zip file
        for filename in archive.namelist():
            # Individual recipes inside use the .paprikarecipe extension
            if filename.endswith(".paprikarecipe"):
                with archive.open(filename) as compressed_file:
                    try:
                        # Decompress the nested Gzip file data
                        with gzip.GzipFile(fileobj=compressed_file) as gf:
                            recipe_data = json.loads(gf.read().decode("utf-8"))

                            # Extract the ingredients string
                            ingredients_raw = recipe_data.get("ingredients", "")
                            return(ingredients_raw)
                    except (json.JSONDecodeError, OSError) as e:
                        print(f"Could not parse recipe {filename}: {e}")



    # print(ingredients_list)  # Print the list of ingredients after processing