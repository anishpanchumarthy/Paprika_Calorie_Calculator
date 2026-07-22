import requests
from dotenv import load_dotenv
import json
import os

load_dotenv('/Users/anishpanchumarthy/Projects/Github/Paprika_Calorie_Calculator/apikeys.env')

url = 'https://api.nal.usda.gov/fdc/'
api_key = os.getenv('API_KEY')
headers = {"X-API-Key": api_key}

def get_USDA_id(food_name,):
    """Get the USDA ID for a given food name.
    input: food_name (str): The name of the food item to search for.
    output: fdcId (int): The USDA ID of the food item, or None if not found.
    """
    #append the food name to the search URL and searches foundation and branded data types, returning the fdcId of the first result
    search_url = f"{url}v1/foods/search?query={food_name}&pageSize=1&dataType=Foundation,Branded&sortBy=dataType.keyword&sortOrder=desc"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['foods']:
            return data['foods'][0]['fdcId']
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None
