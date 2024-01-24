import matrix
from matrix import Matrix

prisn_dilem=Matrix(player1_strats=["Snitch", "Don't Snitch"], 
                   player2_strats=["Snitch", "Don't Snitch"])
print(prisn_dilem)

prisn_dilem.set_player(1,"Bonnie")
prisn_dilem.set_player(2,"Clyde")
print(prisn_dilem)


prisn_dilem.set_strat(2,1,"Tell")
prisn_dilem.set_strat(2,2,"Don't Tell")
print(prisn_dilem)

prisn_dilem.set_payoff("Don't snitch","Don't tell",(1,1))
print(prisn_dilem)
print(prisn_dilem.matrix)

