print("This is the Rock, paper and scissor game. It needs two players to play the game")
print("\n rules: \n\n Rock vs paper->paper wins \n Rock vs Scissor-> Rock wins \n paper vs scissor->scissor wins \n")
print("For Rock use 'R', for paper use 'P' and for Scissor use 'S'\n")
p1 = input("Player1 Enter your Choice(R or P or S): ")
p2 = input("Player2 Enter your Choice(R or P or S): ")

if (p1 == p2):
    print("It's a tie!")
elif ((p1 == "R" and p2 == "P") or (p1 == "P" and p2 == "R")):
    if p1 == 'P':
        print('\nPlayer1 you won!!')
    else:
        print('\nPlayer2 you won!!')
elif ((p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "R")):
    if p1 == 'R':
        print("\nPlayer1 you won!!")
    else:
        print("\nPlayer2 you won!!")
elif ((p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "S")):
    if p1 == 'S':
        print("\nPlayer1 you won!!")
    else:
        print("\nPlayer2 you won!!")
else:
    print("You both kept the same or entered an invalid character")
