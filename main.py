from static.PokemonGold.mapping import town_to_hex, hex_to_FSP
from utils import Map
import os

ROM_PATH = "static/PokemonGold/gold.gbc"

if __name__ == '__main__':

    with open(ROM_PATH, 'rb') as gold_rom:

        # Let's try to create Pallet Town
        pallet_town   = Map(name = "Bedroom", mapping = town_to_hex )
        #pallet_town   = Map(name = "Pallet Town", mapping = town_to_hex )
        bytes_to_read = pallet_town.end - pallet_town.start 


        # Skip to where pallet_town is stored on the ROM
        all_data = gold_rom.read()
        relevant_hex_data = all_data[ pallet_town.start : pallet_town.end ]

        for h in relevant_hex_data:
            offset = hex(pallet_town.end - bytes_to_read)
            bytes_to_read -= 1

            FSP_repr = hex_to_FSP.get(h)

            print("{}    {}   {}".format(offset, hex(h), FSP_repr))


        #print(pallet_town.name, pallet_town.start, pallet_town.end)



