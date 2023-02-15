
import pprint
import requests as req
import sys

def fetch_poke_info(arg):
    """
    Retrieves Pokemon Information

    :param pokename: Name of Pokemon
    :param pokedex_num: Num of Pokemon in Pokedex
    :returns: Dictionary of Pokemon Info
    """
    # Clean up the Pokemon input
    arg_str = str(arg)
    clean_arg = arg.strip()
    clean_arg = clean_arg.lower()
    # See if the Pokemon name was passed or the Pokedex number
    print(f"Getting {clean_arg.title()}'s Information...", end='')
    poke_info = req.get(f'https://pokeapi.co/api/v2/pokemon/{clean_arg}')
    # Check if the reponse succeded
    if poke_info.status_code == req.codes.ok:
        print('Success')
        poke_dict = poke_info.json()
        return poke_dict
    else:
        print('Failure')
        print(poke_info)
        return None
    
