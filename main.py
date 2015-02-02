from static.PokemonGold.mapping import town_to_hex, hex_to_FSP
from utils import Map
import os

ROM_PATH = "static/PokemonGold/gold.gbc"

if __name__ == '__main__':

    with open(ROM_PATH, 'rb') as gold_rom:

        # Let's try to create Pallet Town
        pallet_town   = Map( name ="Pallet Town", mapping = town_to_hex )
        bytes_to_read = pallet_town.end - pallet_town.start 


        # Skip to where pallet_town is stored on the ROM
        gold_rom.seek(pallet_town.start)


        while(True):

            bytes_to_read -= 1
            byte = gold_rom.read(1)
            offset = hex(pallet_town.end - bytes_to_read - 1)

            FSP_repr = hex_to_FSP.get(byte)
            if FSP_repr:
                byte = FSP_repr


            print("{}    {}".format(offset, byte))

            if (int(offset, 16) == pallet_town.end):
                break


            
        #print(pallet_town.name, pallet_town.start, pallet_town.end)


