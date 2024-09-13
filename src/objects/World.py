from objects import Orb, Star, Planet, Moon

class World():
    def __init__(self):
        self.orbs = []
        
    def add_orbs(self, orbs):
        self.orbs.extend(orbs)
