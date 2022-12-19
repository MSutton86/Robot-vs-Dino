class Battlefield:
    def __init__(self, run, display_welcome, battle_phase, display_winner):
        self.fightcommand = display_welcome
        self.mode_fight = battle_phase
        self.champ_decided = display_winner


    def commence(self, fight_begin):
        self.fightcommand == fight_begin
    
    def battle(self, battle):
        self.mode_fight == battle

    def champ(self, decided):
        self.champ_decided == decided