'''Modul'''
import random
from player import Player
from Action import Action

# geeksforgeeks
def most_frequent(list_freq):
    '''Finds the most frequent element in a list'''
    counter = 0
    num = list_freq[0]

    for i in list_freq:
        curr_frequency = list_freq.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


class Historian(Player):
    '''Historian class'''


    def __init__(self, remember):
        self.remember = remember
        self.opponent_choices = []


    def select_action(self):
        counter_list = []
        if self.remember >= len(self.opponent_choices):
            return Action(random.randint(0,2))
        subseq = self.opponent_choices[len(self.opponent_choices)-self.remember:]

        double_list = \
            [self.opponent_choices[x:x+self.remember] for x in range(0, len(self.opponent_choices))]
        for action in range(len(double_list)):
            if  double_list[action] == subseq:
                if len(double_list) <= action+2:
                    continue
                counter_list.append(double_list[action+1][-1])

        if len(counter_list)==0:
            return Action(random.randint(0, 2))

        return Action(most_frequent(counter_list).who_beats_me())

    def receive_result(self, action):
        self.opponent_choices.append(action)

    def enter_name(self):
        return "Historian"
