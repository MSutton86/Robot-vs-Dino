from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 179
        self.active_weapon = Weapon('nades launcher', 48)

    



    def attack(self, dinosaur):
        if self.aint_dead_yet():
            aint_dead_yet = self.health >= 0 
            print(f'{self.name} attacks {dinosaur.name}')

