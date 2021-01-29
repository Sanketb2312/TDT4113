from SingleGame import SingleGame
from Random import Random
from MostCommon import MostCommon
class Tournament:

    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games

    def arrange_singlegame(self):
        s = SingleGame(self.player1, self.player2)
        s.show_result()

    def arrange_tournament(self):
        player_1_wins = 0
        player_2_wins = 0
        for game in range(self.number_of_games):
            s = SingleGame(self.player1, self.player2)
            winner = s.playGame()
            s.show_result()
            print(winner, ": winner")
            if(winner == self.player1):
                player_1_wins+=1
        print(player_1_wins)


p = Random()
p2 = MostCommon()
t = Tournament(p, p2, 5)
t.arrange_tournament()


