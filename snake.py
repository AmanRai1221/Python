'''
1 for snake   s
-1 for water  w
0 for gun  g
'''
import random
computer = random.choice([-1,0, 1])
# computer = -1
youstr = input("Enter your choice: ")
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}
you = youDict[youstr]

print(f"You chose {youstr} and computer chose {computer}")

if(computer == you):
    print("Draw")

else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("Computer wins")
    elif(computer == 1 and you == -1):
        print("Computer wins")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("Computer wins")
    else:
        print("Somthing went wrong")