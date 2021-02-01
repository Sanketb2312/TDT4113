'''Modul'''
from random_player import Random
from Sequential import Sequential
from Action import Action
from historian import Historian
from most_common import MostCommon
class SingleGame:
    '''Singlae_game class'''
    action1 = None
    action2 = None
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def playGame(self):
        '''playgame method'''

        self.action1 = self.player1.select_action()
        self.action2 = self.player2.select_action()

        if isinstance(self.player1, (MostCommon, Historian)):
            self.player1.receive_result(self.action2)
        if isinstance(self.player2, (MostCommon, Historian)):
            self.player2.receive_result(self.action1)

        if self.action1 > self.action2:
            return self.player1
        elif self.action2 > self.action1:
            return self.player2
        else:
            return None

    def show_result(self):
        '''showing result'''
        game = self.playGame()
        if game == self.player1:
            print("Player 1 won the game. Player 1 chose ",
                  self.action1 ," and Player 2 chose ", self.action2)
            return self.player1
        elif game == self.player2:
            print("Player 2 won the game. Player 2 chose ",
                  self.action2 ," and Player 1 chose ", self.action1)
            return self.player2
        elif game == None:
            print("It is a tie. Player 1 and Player 2 both chose", self.action2)
            return None

"""p1 = Historian(2)
p2 = Random()
p = SingleGame(p1, p2)
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")
p.show_result()
print("\n")"""



