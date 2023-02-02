import random

def game():
  #player = input("Enter your choice (rock,paper,scissor): ")
  player="paper"
  choices = ["rock","paper","scissor"]
  computer = random.choice(choices)
  choiceDict = {"player":player,"computer":computer}
  return choiceDict



def check_win(player,computer):
  print(f"***you chose {player}***")
  print(f"**computer chose {computer}**")
  if player==computer:
    return "It's a tie!"
  elif player=="rock": 
    if computer=="scissor":
      return "Player won!"
    else:
      return "Computer won!"
  elif player=="scissor":
    if computer=="paper":
      return "Player won!"
    else:
      return "Computer won!"
  else:
    if computer=="scissor":
      return "Computer won!"
    else:
      return "Player won!"
    
    

choices=game() # it'll be a dictionary just like before

choiceA=choices["player"]
choiceB=choices["computer"]

result=check_win(choiceA,choiceB)
print(result)
print("*****")
age=0
print(f"Jim is {age} years old")
if age>=19:
  print("You're an adult!")
elif age>=12 and age<=18:
  print("You're a teenager")
elif age<=11 and age>1:
  print("You're a child")
else:
  print("You're a baby")
"""
a=3
b=1
if a>b: # ==  != <= >=
  print ("a is bigger")
else:
  print ("b is bigger")


"""
