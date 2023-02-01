import random

def game_e():
  player = input("Enter your choice (rock,paper,scissor,lizard): ")
  choices = ["rock","paper","scissor","lizard"]
  computer = random.choice(choices)
  choiceDict = {"Player":player,"Computer":computer}
  return choiceDict