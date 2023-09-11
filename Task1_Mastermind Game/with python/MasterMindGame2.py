import random
player = random.randint(1,10)

pl_ts=0
opp_ts=0
if(player%2==0):
    opponent=1
    player =1
else:
    opponent=2
    player=1
pl_score,opp_score = 0,0
players = {player:pl_score, opponent:opp_score}

for curr in players.keys():
    isTrue=True
    pl_num = int(input(f"\n\nPlayer{curr} please enter a Multi-Digit Number: "))
    pl_num = str(pl_num)
    if(curr%2==0):
        opponent=1
    else:
        opponent=2
    while(isTrue):
        print(f"\n Player{opponent} guess the number. It is a {len(pl_num)} digit number \n")
        opp_num = int(input("\n Enter your guess: "))
        opp_num = str(opp_num)
        g_p=0
        pl_ts+=1
        for i in range(len(pl_num)):
            if (pl_num[i] == opp_num[i]):
                print(opp_num[i],end="\t")
                g_p +=1;
            else:
                print('_', end='\t')
        if(g_p==len(pl_num)):
            print('\n\n Excellent you guessed right!')
            if(pl_ts == 1):
                print(f"\n Congrats Mastermind! player{curr} you won in first attempt itself!!!")
                exit(0);
            isTrue=False
        else:
            print('\n\n try again')
        
    print("The number of times you tried: ",pl_ts)
    players[curr]=pl_ts
    pl_ts=0


if(opp_ts<pl_ts):
    print(f"\n Congrats Mastermind! player{opponent} you won")
else:
    print(f"\n Congrats Mastermind! player{player} you won")

