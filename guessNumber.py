import random 

def guessNumber():
    print("""    Hey hey, let's play a game ! 
    I will choose secretly an integer number between 1 and 9
    if you guess the right number in less than 5 tries, you win !""")
    max_tries_number = 5
    secret_number = random.randint(1,9)
   
    not_guessed = True
    guesses_number = 1
    while not_guessed and guesses_number < max_tries_number + 1:
        if guesses_number == 1:
            guessed_number = int(input("Enter a number: "))
        elif max_tries_number-guesses_number+1 == 1:
            guessed_number = int(input(f"It was not the correct number, last chance ! , enter a value: "))
        else:
            guessed_number = int(input(f"It was not the correct number, you still have {max_tries_number-guesses_number+1}, enter a new value: "))

        if guessed_number == secret_number:
            print(f"You won with {guesses_number} trie(s) !! Congrats!")
            break
      
        guesses_number += 1

    else:
        print(f"You lost :( the secret number was {secret_number}, but you can re-play ;) have fun !!")








if __name__ == "__main__":
    guessNumber()