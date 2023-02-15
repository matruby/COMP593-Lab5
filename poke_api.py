
import pprint
import requests as req
import sys


def fetch_poke_info(pokename="", pokedex_num=""):
    """
    Retrieves Pokemon Information

    :param pokename: Name of Pokemon
    :param pokedex_num: Num of Pokemon in Pokedex
    :returns: Dictionary of Pokemon Info
    """
    # See if the Pokemon name was passed or the Pokedex number
    if pokename:
        print(f"Getting {pokename.title()}'s Information!!\n")
        poke_info = req.get(f'https://pokeapi.co/api/v2/pokemon/{str(pokename)}')
        # Check if the reponse succeded
        if poke_info.status_code == req.codes.ok:
            print(f'{pokename.title()} Found!\n'
            poke_dict = poke_info.json()
        else:
            print(f"{pokename.title()} Doesn't Exist!\nRetry with a valid Pokemon!")
            return None
    
    if pokedex_num:
        print(f"Getting {pokename.title()}'s Information!!\n")
        poke_info = req.get(f'https://pokeapi.co/api/v2/pokemon/{str(pokedex_num)}')
        # Check if the reponse succeded
        if poke_info.status_code == req.codes.ok:
            print(f'{pokename.title()} Found!\n')
            poke_dict = poke_info.json()
        else:
            print(f"{pokename.title()} Doesn't Exist!\nRetry with a valid Pokemon!")
            return None
 
    return poke_dict


