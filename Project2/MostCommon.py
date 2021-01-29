from Player import Player
from Action import Action
import random


# geeksforgeeks
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

class MostCommon(Player):

    opponent_choices=[]

    def select_action(self):
        counter_attack = self.get_opponents_most_common_actions()
        if(isinstance(counter_attack, Action)):
            return Action(counter_attack.who_beats_me())
        return Action(counter_attack)


    def receive_result(self, action):
        self.opponent_choices.append(action)


    def enter_name(self):
        return"MostCommon"


    def get_opponents_most_common_actions(self):
        if(len(self.opponent_choices)==0):
            return random.randint(0,2)
        else:
            return most_frequent(self.opponent_choices)
