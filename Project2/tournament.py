'''Modul'''
import matplotlib. pyplot as plt
from single_game import SingleGame
from random_player import Random
from most_common import MostCommon
from Sequential import Sequential
from historian import Historian

class Tournament:
    '''Tournament class'''

    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games

    def arrange_singlegame(self):
        s = SingleGame(self.player1, self.player2)
        s.playGame()
        s.show_result()

    def arrange_tournament(self):
        player_1_winpercentage = []
        player_1_wins = 0
        for game in range(self.number_of_games):
            singalegame = SingleGame(self.player1, self.player2)
            wins = singalegame.show_result()
            if wins == self.player1:
                player_1_wins+=1
            elif wins is None:
                player_1_wins+=0.5
            player_1_winpercentage.append(player_1_wins/(game+1))
        plt.plot(player_1_winpercentage)
        plt.show()

p = Historian(2)
p2 = MostCommon()
t = Tournament(p, p2, 150)
t.arrange_tournament()
