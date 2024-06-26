import json
import random

def get_random_quote():
    # Load the JSON data from the file
    with open('quotes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Generate a random number between 1 and 7060
    random_id = random.randint(1, 7060)
    
    # Search for a quote with the matching id
    for quote in data['quotes']:
        if quote['id'] == random_id:
            return quote['text'], quote['source']
    
    # Return a default message if no quote is found with the id
    return "No quote found for the generated ID."
