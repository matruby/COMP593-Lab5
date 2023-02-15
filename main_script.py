
# Get the pokemon name from a command line param
# Fetch pokemon information from the PokeAPI
# If that was succesful determine the title of 
# the new PasteBin pate, then determine the body
# text of the new PasteBin paste, 
# Print the URL of the new PasteBin paste

from poke_api import fetch_poke_info
from paste_bin_api import post_new_paste
import sys

def main():
    """Run all of the script functions from this function"""
    poke_name = get_poke_name() # Pokemon name from command line arg
    paste_title = create_paste_title(poke_name) # PasteBin paste title
    pokemon_info= fetch_poke_info(poke_name) # Get the JSON from PokeAPI
    paste_body = create_paste_body(pokemon_info) # PasteBin paste body_text
    paste_url = post_new_paste(paste_title, paste_body) # Paste information 
    print(paste_url)

def get_poke_name():
    """Gets pokemon name from command line args"""
    args = sys.argv    
    # Check if there is args given
    if len(args) <= 1:
        print("No command line arguments given!\nTry again!")
        sys.exit()
    # Check if there's too many args given
    elif len(args) > 2:
        print("Too many command line arguments given!\nTry again!")
        sys.exit()
    # Return the pokemon name
    else:
        return args[1]

def create_paste_title(name):
    """Creates the title for the new paste"""
    return f"{name.title()}'s Abilities"

def create_paste_body(poke_dict):
    """Construct paste body text from Dictionary"""
    # String for the paste body
    all_abilities = ''
    # Get all of the abilities
    poke_abilities = poke_dict['abilities']
    # Loop over them and add the proper string sections to all_abilities
    for count, entry in enumerate(poke_abilities):
        if count + 1 == len(poke_abilities):
            all_abilities += f"- {entry['ability']['name']}"
        else:
            all_abilities += f"- {entry['ability']['name']}\n"
        
    return all_abilities

if __name__ == '__main__':
    main()

