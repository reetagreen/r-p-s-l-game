import random

def game():
  #player = input("Enter your choice (rock,paper,scissor,lizard): ")
  player="scissors"
  choices = ["rock","paper","scissor","lizard"]
  computer = random.choice(choices)
  choiceDict = {"Player":player,"Computer":computer}
  return print(choiceDict)

game()

def check_win(player,computer):
  print(f"***you chose {player}***")
  print(f"**computer chose {computer}**")
  if player==computer:
    return "It's a tie!"

age=25
print(f"Jim is {age} years old")

"""
a=3
b=1
if a>b: # ==  != <= >=
  print ("a is bigger")
else:
  print ("b is bigger")
"""
