 
class Normal_Game:

    def __init__(self):
        self.players=[]
        self.strats=[]
        self.payoffs=[]

    #---  ACCESORS & MUTATORS  ---#
    def get_players(self):
        return self.players
    
    def get_strats(self):
        return self.strats    
    
    def get_payoffs(self):
        return self.payoffs
    
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)