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

    opponent_choices = []
    counter_list = []

    def __init__(self, remember):
        self.remember = remember


    def select_action(self):
        if self.remember >= len(self.opponent_choices):
            return Action(random.randint(0,2))
        subseq = self.opponent_choices[len(self.opponent_choices)-self.remember:]
        #print([str(x) for x in subseq], " subseq")
        double_list = \
            [self.opponent_choices[x:x+self.remember] for x in range(0, len(self.opponent_choices))]
        #print([[str(x) for x in i] for i in double_list], " double list")
        #print([str(x) for x in self.opponent_choices], " opponent")
        for action in range(len(double_list)):
            if(double_list[action] == subseq):
                if(len(self.opponent_choices) <= action+2):
                    continue
                self.counter_list.append(double_list[action+1][-1])
            #print([str(x) for x in self.counter_list], " counterlist")


        if(len(self.counter_list)==0):
            return Action(random.randint(0, 2))
        a = Action(most_frequent(self.counter_list).who_beats_me())
        #print(a)
        return a

    """counter_attack_list = []
    
    def select_action(self):
        if(self.remember >= len(self.opponent_choices)):
            return Action(random.randint(0,2))
        subseq = self.opponent_choices[len(self.opponent_choices)-self.remember:]
        counter_sub = 0
        print([str(x) for x in subseq], " subseq")
        for x in range(len(self.opponent_choices)):
            print([str(x) for x in self.opponent_choices], " opponent")
            if(self.opponent_choices[x]==subseq[counter_sub]):
                counter_sub += 1
                print(counter_sub)
                if(counter_sub == self.remember):
                    counter_sub = 0
                    if(x+1 < len(self.opponent_choices)):
                        self.counter_attack_list.append(self.opponent_choices[x+1])
            else:
                counter_sub=0
            print([str(x) for x in self.counter_attack_list], " counterattack")
        if(len(self.counter_attack_list) == 0):
            return Action(random.randint(0,2))
        return Action(most_frequent(self.counter_attack_list).who_beats_me())"""




    def receive_result(self, action):
        self.opponent_choices.append(action)

    def enter_name(self):
        return "Historian"

