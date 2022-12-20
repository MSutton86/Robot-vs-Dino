class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 159
        self.attack_power = 54
        

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacks {robot.name}')

    