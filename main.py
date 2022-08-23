#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo


print(logo)
print("I'm a number between 0 to 100 😎. Find me 😌.")
guess_number=round(random.uniform(0, 100))

diff=input("Choose a difficulty level. (easy,hard): ").lower()
guess=0
if diff=="easy":
  guess+=10
elif diff=="hard":
  guess+=5

def choice(guess_number):
  question=int(input("Make a guess: "))
  if question==guess_number:
    return "You found me😍"
  elif question>guess_number:
    return "Too high"
  elif question<guess_number:
    return "Too low" 
    
for value in range(guess):  
  answer=choice(guess_number)
  print(answer)
  if answer=="You found me😍":
    break
  if answer=="Too high" or "Too low":
    val=guess-((value+1))
    print(f"You have {val} to guess the number")
  if val==0 and answer!="You found me😍":
    print("Sorry guess me later😭")
  




  
  



