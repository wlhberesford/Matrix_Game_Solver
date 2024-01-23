import matrix
from matrix import Matrix

prisn_dilem=Matrix(player1_strats=["Snitch", "Don't Snitch"], player2_strats=["Snitch", "Don't Snitch"])
print(prisn_dilem)

print(prisn_dilem.get_player(1))
print(prisn_dilem.get_strats(player_num=2))
print(prisn_dilem.get_strats(player="Player 1"))

print(prisn_dilem.get_matrix())

prisn_dilem.set_player(1,"Bonnie")
prisn_dilem.set_player(2,"Clyde")

prisn_dilem.set_strat(1,1,"Tell")
prisn_dilem.set_strat(1,2,"Don't Tell")

prisn_dilem.set_payoff("Tell", "Snitch", (-10,-8))

print(prisn_dilem)



