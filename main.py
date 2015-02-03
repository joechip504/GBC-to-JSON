from static.PokemonGold.mapping import town_to_hex, hex_to_FSP
from utils import Map, Block
import os
import sys

ROM_PATH = "static/PokemonGold/gold.gbc"
SQUARE_SIZE = 8

if __name__ == '__main__':

    with open(ROM_PATH, 'rb') as gold_rom:

        # Let's try to create your Bedroom in Pallet Town

        current_map = Map(name = "Ash's Room", mapping = town_to_hex,
                width = 4, height = 9)

        bytes_to_read = current_map.end - current_map.start 


        # Skip to where pallet_town is stored on the ROM
        ### NEED TO DOUBLE CHECK THE ADDING 1 HERE

        all_data = gold_rom.read()
        relevant_hex_data = all_data[ current_map.start : current_map.end + 1 ]


        #i, j = 550, 350 
        i, j = 0, 0 
        i_ = 0

        for h in relevant_hex_data:
            offset = hex(current_map.end - bytes_to_read)
            bytes_to_read -= 1

            FSP_repr = hex_to_FSP[current_map.bank].get(h)
            b = Block(FSP_repr, i, j)
            
            current_map.add_block(b)

            i += 8 
            i_ += 1
            if (i_ % current_map.width == 0):
                i_ = 0
                i -= 8 * current_map.width
                j += 8 



        print(current_map.FSP_map())


        


        #print(pallet_town.name, pallet_town.start, pallet_town.end)



