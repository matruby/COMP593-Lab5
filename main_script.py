
# Get the pokemon name from a command line param
# Fetch pokemon information from the PokeAPI
# If that was succesful determine the title of 
# the new PasteBin pate, then determine the body
# text of the new PasteBin paste, 
# Print the URL of the new PasteBin paste

import sys

def main():
    """Run all of the script functions from this function"""
    poke_name = get_poke_name()
    paste_title = create_paste_title(poke_name)


def get_poke_name():
    """Gets pokemon name from command line args"""
    args = sys.argv
    
    # Check if there is args given
    if len(args <= 1):
        print("No command line arguments given!\nTry again!")
        sys.exit()
    # Check if there's too many args given
    elif len(args > 3):
        print("Too many command line arguments given!\nTry again!")
        sys.exit()
    # Return the pokemon name
    else:
        return args[1]

def create_paste_title(name):
    """Creates the title for the new paste"""
    return f"{name.title()}'s Abilities"



