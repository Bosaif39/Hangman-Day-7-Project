import random

# List of possible words
word_bank = [
    "adventure", "ardvark", "butterfly", "chocolate", "dolphin", "elephant",
    "fashion", "giraffe", "horizon", "incredible", "jungle", "kiwi",
    "library", "mystery", "notebook", "octopus", "puzzle", "quasar",
    "rainbow", "sapphire", "telescope", "umbrella", "vaccine", "whale",
    "xylophone", "yacht", "zebra", "zeppelin", "acrobatic", "bicycle",
    "calendar", "dinosaur", "exquisite", "flamingo", "guitar", "hologram",
    "internet", "jigsaw", "kangaroo", "lighthouse", "moonlight", "ninja",
    "original", "paradise", "quarantine", "robotics", "snowflake", "trampoline",
    "unicorn", "volcano", "waterfall", "xenon", "yogurt", "zoology"
]

# Pick a random word
secret_word = random.choice(word_bank)
word_length = len(secret_word)

# Underscore placeholders for each letter
current_progress = ['_'] * word_length
print(current_progress)

remaining_lives = 6

# Keep track of guessed letters
used_letters = []

# Main game loop: runs until player wins or loses
while '_' in current_progress:
    print(f"You have {remaining_lives} lives left")
    player_guess = input("Guess a letter: ").lower()
    
    for i in range(word_length):
        if secret_word[i] == player_guess:
            current_progress[i] = player_guess
            print(current_progress)

            if '_' not in current_progress:
                print("You win")
                break  
    
    if player_guess in used_letters:
        print(f"You already guessed the letter '{player_guess}'")
    
    elif player_guess not in secret_word:
        print(f"The letter '{player_guess}' is not in the word")
        used_letters.append(player_guess)  
        remaining_lives -= 1
        
        if remaining_lives == 0:
            print(f"You lose, the word was '{secret_word}'")
            break
