from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur('Blue')
        self.robot = Robot('T1K')


    def display_welcome(self):
        print('Greetings mortals!')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            

    def display_winner(self):
        if self.dinosaur.health > 0:
            print('{self.dinosaur.name} is the winner') 
        elif self.robot.health > 0:
            print('{self.robot.name} is the winner')

