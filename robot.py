from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 179
        self.active_weapon = Weapon('nades launcher', 48)

    



    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacks {dinosaur.name}')

