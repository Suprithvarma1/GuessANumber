from random import randint
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


 #FUNCTION TO CHECK USERS GUESS AGAINST ACTUAL ANSWER
def check_answer(guess,answer,turns):
    """checks answer against guess.Returns the number of turns remaining."""
    if guess > answer:
        print("Too High.")
        return turns-1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():


#choosing a random num from 1 and 100
 print(logo)
 print("Welcome To The Number Guessing Game...!")
 print("I'm thinking of a number between 1 and 100.")
 answer=randint(1,100)
 #print(f"The Correct answer is {answer}")

 turns=set_difficulty()

 guess=0
#LET THE USER GUESS THE NUMBER

 while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess=int(input("Make a Guess:"))
    turns=check_answer(guess,answer,turns)
    if turns==0:
       print("You've run out of guesses,you lose.")
       return
    elif guess!=answer:
     print("Guess Again!")

game()
