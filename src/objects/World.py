from objects import Orb, Star, Planet, Moon

class World():
    def __init__(self):
        self.orbs = []
        
    def add_orbs(self, orbs):
        if not isinstance(orbs, list):
            orbs = [orbs]
        
        for orb in orbs:
            if orb in self.orbs:
                continue
            
            if isinstance(orb, Star):
                print(f"{orb} jest słońcem (Star)")
                self.orbs.append(orb)
                self.add_orbs(orb.planets)
                
            elif isinstance(orb, Planet):
                print(f"{orb} jest planetą (Planet)")
                self.orbs.append(orb)
                self.add_orbs(orb.moons)
                
            else:
                print(f"{orb} nie jest słońcem (Star), ale jest instancją klasy {type(orb).__name__}")
                self.orbs.append(orb)
