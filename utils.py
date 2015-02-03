class Map(object):
    def __init__(self, name = None, mapping = {}, 
            width = 4, height = 4, bank = None):

        self.name  = name
        self.width = width
        self.height = width

        self.bank =  mapping.get(name)[2]
        self.start = int(mapping.get(name)[0], 16)
        self.end   = int(mapping.get(name)[1], 16)



        self.blocks = []

    def FSP_map(self):
        '''
        For now, this is designed to go in the 'contents' section.
        '''
        javascript = [b.FSP_JSON() for b in self.blocks]
        return ','.join(javascript)


    def add_block(self, block):
        self.blocks.append(block)


class Block(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {}) {}".format(self.x, self.y, self.name)


    def FSP_JSON(self):
        '''
        { "thing": "PottedPalmTree", "x": 48, "y": 48 }
        '''

        # For now, default unknown tiles to dirt
        if not(self.name):
            self.name = "DirtMedium"


        json = '''
        {{"thing": "{0}", "x": {1}, "y": {2} }}'''.format(
                self.name, self.x, self.y)

        return json
    
