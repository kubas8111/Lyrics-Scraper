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
                # print(f"{orb} jest słońcem (Star)")
                self.orbs.append(orb)
                self.add_orbs(orb.planets)
                
            elif isinstance(orb, Planet):
                # print(f"{orb} jest planetą (Planet)")
                self.orbs.append(orb)
                self.add_orbs(orb.moons)
                
            else:
                # print(f"{orb} jest księżycem (Moon)")
                self.orbs.append(orb)
                
            print(f"Added {orb.name} to world")

    def setup_forces(self):
        for orb in self.orbs:
            if isinstance(orb, Star):
                for planet in orb.planets:
                    planet.apply_father_velocity()
                    for moon in planet.moons:
                        moon.apply_father_velocity()
