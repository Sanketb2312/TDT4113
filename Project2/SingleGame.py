from Random import Random
from Sequential import Sequential
from Action import Action
from MostCommon import MostCommon
class SingleGame:
    action1 = None
    action2 = None
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def playGame(self):
        self.action1 = self.player1.select_action()
        self.action2 = self.player2.select_action()

        if(self.action1 > self.action2):
            self.player1.receive_result(self.action2)
            return self.player1
        elif(self.action2 > self.action1):
            self.player2.receive_result(self.action1)
            return self.player2
        else:
            self.player1.receive_result(self.action2)
            self.player2.receive_result(self.action1)
            return None

    def show_result(self):
        game = self.playGame()
        if(game == self.player1):
            print("Player 1 won the game. Player 1 chose ", self.action1 ," and Player 2 chose ", self.action2)
        elif(game == self.player2):
            print("Player 2 won the game. Player 2 chose ", self.action2 ," and Player 1 chose ", self.action1)
        elif (game == None):
            print("It is a tie. Player 1 and Player 2 both chose", self.action2)

p1 = MostCommon()
p2 = Random()
p = SingleGame(p1, p2)
w = p.playGame()
p.show_result()
p.playGame()
p.show_result()
p.playGame()
p.show_result()
p.playGame()
p.show_result()










