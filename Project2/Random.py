from Player import Player
from Action import Action
import random
class Random(Player):

    def select_action(self):
        tmp = random.randint(0,2)
        #print(Action(tmp), " val")
        return Action(tmp)

    def receive_result(self, action):
        pass

    def enter_name(self):
        return "Random"
