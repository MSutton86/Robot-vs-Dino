from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur('Blue')
        self.robot = Robot('T1K')

    def run_game(self):
        pass

    def display_welcome(self):
        print('Greetings mortals!')

    def battle_phase(self):
        aint_dead_yet = self.health <= 0
        if self.dinosaur.aint_dead_yet() and self.robot.aint_dead_yet():
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            
        elif aint_dead_yet != True:
            
            return 

    def display_winner():
        pass
    
    