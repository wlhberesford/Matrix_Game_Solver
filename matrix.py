'''
Class to store information about a 2 player matrix game

stores:
    player names (default: 'Player 1' 'Player 2')
    player's set of stratedgies 
    Payoff Matrix

Users will instanciate a "blank" matrix (all payouts are 0)
with 2 players and all their stratedgies

Then using set_payoff() to set payoffs individually or 
a full matrix

'''


class Matrix:

    def __init__(self, player1="Player 1", player2="Player 2", player1_strats=[], player2_strats=[]):
        self.player1=player1
        self.player2=player2
        self.player1_strats=player1_strats
        self.player2_strats=player2_strats

        self.matrix=[[(0,0)*len(self.player2_strats)]*len(self.player1_strats)]

    def __str__(self):
        pass

    '''     Accessors     '''
    def get_player(self,player_num):
        pass
    def get_strats(self, player="", player_num=-1):
        pass
    def get_matrix(self):
        pass

    '''     Mutators     '''
    def set_player(self, player_num, name):
        pass
    def set_strat(self, player, strat_num):
        pass
    def set_payoff(self, p1_strat, p2_strat, payoff):
        pass
    def set_payoff(self, matrix):
        pass

