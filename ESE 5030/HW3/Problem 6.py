import random

def flip_coin(p):
    rand_num=random.random()

    return rand_num<=p

p=[(0.3,0.3),(0.9,0.3),(0.5,0.5),(0.2,0.9)]
def who_wins(pa,pb):
    round_on=True
    num_rounds=0
    while round_on:
        num_rounds+=1
        if flip_coin(pa):
            return 1,num_rounds
        elif flip_coin(pb):
            return 0,num_rounds

for pa,pb in p:
    num_simulations=4000
    num_a_wins=0
    num_b_wins=0
    num_rounds=0
    for i in range(num_simulations):
        w,rounds=who_wins(pa,pb)
        if w==1:
            num_a_wins+=1
        else:
            num_b_wins+=1
        num_rounds+=rounds
        
    print(f"For pa={pa} and pb={pb}")
    print(f"Probability A wins={num_a_wins/num_simulations}")
    print(f"Probability B wins={num_b_wins/num_simulations}")
    print(f"Average number of rounds till a win={num_rounds/num_simulations}")

