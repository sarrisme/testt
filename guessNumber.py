from curses.ascii import isdigit
from email import message
import random 

def guessNumber():
    print("""    Hey hey, let's play a game ! 
    I will choose secretly an integer number between 1 and 9
    if you guess the right number in less than 5 tries, you win !""")
    max_tries_number = 5
    min_boundary = 1
    max_boundary = 9
    secret_number = random.randint(min_boundary,max_boundary)
   
    
    guesses_number = 1
    while guesses_number < max_tries_number + 1:
        
        if guesses_number == 1:
            guessed_number = input("Enter a number: ")
        elif max_tries_number-guesses_number+1 == 1:
            guessed_number = input(f"It was not the correct number, last chance ! , enter a value: ")
        else:
            guessed_number = input(f"It was not the correct number, you still have {max_tries_number-guesses_number+1} tries, enter a new value: ")
        
        checked_number, error_message = checkInput(guessed_number, min_boundary, max_boundary)
        if checked_number:
            if int(guessed_number) == secret_number:
                print(f"You won with {guesses_number} trie(s) !! Congrats!")
                break      
            guesses_number += 1
        else:
            print(error_message)
    else:
        print(f"You lost :( the secret number was {secret_number}, but you can re-play ;) have fun !!")


def checkInput(player_input, min_boundary, max_boundary):
    check_flag = True
    error_message = None
    accepted_values = [i for i in range(min_boundary, max_boundary+1)]
    try:
        if int(player_input) not in accepted_values:
            check_flag = False
            error_message = f"The entered number is not between {min_boundary} and {max_boundary} !"
    except ValueError:
        check_flag = False
        error_message = "Please enter a numeric value !"       
    return check_flag, error_message





if __name__ == "__main__":
    guessNumber()