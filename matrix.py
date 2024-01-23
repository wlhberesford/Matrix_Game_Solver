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

        self.matrix=[[(0,0)]*len(self.player2_strats)]*len(self.player1_strats)

    def __str__(self):
        players="Player 1: {}\t{}\nPlayer 2: {}\t{}\n".format(self.player1,self.player1_strats,self.player2,self.player2_strats)
        line="-"*(len(self.player2_strats)*8+1)+"\n"
        mat=line
        for i in range(len(self.player1_strats)):
            mat+="|"
            for j in range(len(self.player2_strats)):
                mat+= " {} , {} |".format(self.matrix[i][j][0],self.matrix[i][j][0])
            mat+="\n"
            mat+=line
        return players+mat

    '''     Accessors     '''
    def get_player(self,player_num=-1):
        if player_num==1:
            return self.player1
        elif player_num==2:
            return self.player2
        
    def get_strats(self, player="", player_num=-1):
        if player=="":
            if player_num==1:
                return self.player1_strats
            elif player_num==2:
                return self.player2_strats
        elif player_num==-1:
            if player==self.player1:
                return self.player1_strats
            elif player_num==self.player2:
                return self.player2_strats

    def get_matrix(self):
        return self.matrix

    '''     Mutators     '''
    def set_player(self, player_num, name):
        if player_num==1:
            self.player1=name
        elif player_num==2:
            self.player2=name

    def set_strat(self, player_num, strat_num, strat):
        if player_num==1:
            self.player1_strats[strat_num]=strat
        elif player_num==2:
            self.player2_strats[strat_num]=strat

    def set_payoff(self, p1_strat, p2_strat, payoff):
        self.matrix[self.player1_strats.index(p1_strat),self.player2_strats.index(p2_strat)]=payoff
    
    def set_payoff(self, matrix):
        self.matrix=matrix

