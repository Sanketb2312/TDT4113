'''Module'''
import random
from player import Player
from action import Action


# geeksforgeeks
def most_frequent(freq_list):
    '''finds the most frquent element in a list'''
    counter = 0
    num = freq_list[0]

    for i in freq_list:
        curr_frequency = freq_list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num

class MostCommon(Player):
    '''MostCommon class'''

    opponent_choices=[]

    def select_action(self):
        counter_attack = self.get_opponents_most_common_actions()
        if isinstance(counter_attack, Action):
            return Action(counter_attack.who_beats_me())
        return Action(counter_attack)


    def receive_result(self, action):
        self.opponent_choices.append(action)


    def enter_name(self):
        return"MostCommon"


    def get_opponents_most_common_actions(self):
        '''uses the most_frequent method to return opponents most common action'''
        if len(self.opponent_choices)==0:
            return random.randint(0, 2)
        return most_frequent(self.opponent_choices)
