class Map(object):
    def __init__(self, name = None, mapping = {}):
        self.name  = name

        self.start = int(mapping.get(name)[0], 16)
        self.end   = int(mapping.get(name)[1], 16)

        self.blocks = []

    def generate_FSP_map(self):
        pass

class Block(object):
    def __init__(self):
        pass


    def generate_FSP_object(self):
        pass
    
