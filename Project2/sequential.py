'''Modul'''
from player import Player
from Action import Action
class Sequential(Player):
    '''Sequential class'''

    counter = -1
    def select_action(self):
        self.counter += 1
        if self.counter > 2:
            self.counter = 0
            return Action(self.counter)
        return Action(self.counter)

    def receive_result(self, action):
        pass

    def enter_name(self):
        return "Sequential"