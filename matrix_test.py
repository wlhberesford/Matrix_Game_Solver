import matrix
from matrix import Matrix

def pd_test():
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

def threebythreeTest():
    p1_plays=["Rock","Paper",'Scissors']
    p2_plays=["Rock","Paper",'Scissors']
    rps_game=Matrix(player1_strats=p1_plays,player2_strats=p2_plays)

    print(rps_game)

    payoffs=[[(0,0),(-1,1),(1,-1)],
             [(1,-1),(0,0),(-1,1)],
             [(-1,1),(1,-1),(0,0)]]

    rps_game.set_matrix(payoffs)

    print(rps_game)


if __name__=="__main__":
    choice=int(input("(1) Prisoners Dilemna Test\n(2) Rock Paper Scissors\n(3) Both\nWhich test(s) would you like to see: "))

    if(choice==1):
        pd_test()
    elif(choice==2):
        threebythreeTest()
    elif (choice==3):
        pd_test()
        threebythreeTest()


