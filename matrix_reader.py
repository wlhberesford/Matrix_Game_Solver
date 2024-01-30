from matrix import Matrix

class Matrix_Reader:

    def __init__(self, matrix):
        self.game=matrix

    def get_matrix(self):
        return self.game
    
    def set_matrix(self,matrix):
        self.game=matrix

    def get_player_payoff(self,player):
        mat=self.game.get_matrix()
        ret=mat.copy()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ret[i][j]=mat[i][j][player-1]
                  
        return ret


    
       