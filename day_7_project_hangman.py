import random

words = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(words)
wordLen = len(chosen_word)
my_list = ['_'] * wordLen
print(my_list)

lives = 6

#List to keep track of guessed letters
guess_list = []

#Main game loop: continues until the player has guessed all letters or runs out of lives

while '_' in my_list:
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()
    
    for i in range(wordLen):
        if chosen_word[i] == guess:

            my_list[i] = guess
            print(my_list)

            if ('_' not in my_list):
                print("You win")
                break  
    
    if (guess in guess_list):
        print(f"You have used the letter {guess}")
    
    
    elif (guess not in chosen_word):
        print(f"The letter {guess} is not in the word")
        guess_list.append(guess)  
        lives -= 1
        
        if (lives == 0):
            print("You lose")
            break  
