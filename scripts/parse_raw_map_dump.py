### TODO relative imports from ../lib/map.py

import pprint

def dump_to_dict(dump):
    '''
    :param dump: location of raw map dump from datacrystal.romhacking.net, 
                like ../static/PokemonGold/RomMapDump.txt
    :type dump: str or unicode

    :returns: mapping between map name and 2-tuple start and end
    :rtype: dict
    '''

    d = {}

    with open(dump) as f:

        current_bank = None

        for line in f.readlines():

            # Update current_bank, if necessary
            if '=' in line:
                current_bank = '_'.join(line.strip().strip('=').split())
                print(current_bank) # 37_DC000
                continue



            # The dump is messy and has lots of irrelevant lines we can ignore.
            line = line.strip()
            if not(line):
                continue

            # Parse into    name:"Pallet Town", start:"A9497", end:"A94F0" 
            hex_locations, name = line.strip().split(' ', 1)
            start, end = hex_locations.split('-')
            
            d[name] = (start, end, current_bank)

    return d


# Usage
if __name__ == '__main__':
    d = dump_to_dict('../static/PokemonGold/RomMapDump.txt')

    with open("output.py", "w") as f:
        contents = pprint.pformat(d)
        f.write(contents)
