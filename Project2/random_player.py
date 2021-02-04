'''Module'''
from player import Player
from action import Action
import random

class Random(Player):
    '''Random player class'''

    def select_action(self):
        tmp = random.randint(0,2)
        return Action(tmp)

    def receive_result(self, action):
        pass

    def enter_name(self):
        return "Random"
