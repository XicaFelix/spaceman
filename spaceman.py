import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append('_')
    
    # Create a string representation
    return ' '.join(guessed_word)

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    return guess in secret_word
    
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    # Initialize variables
    letters_guessed = []
    attempts = 7  # Allow only 7 incorrect guesses

    secret_word_ll = {}
    for i in range(len(secret_word)):
        letter = secret_word[i]
        if letter not in secret_word_ll:
            secret_word_ll[letter] = [i]
        else:
            secret_word_ll[letter].append(i)

    print("Welcome to Spaceman! Try to guess the secret word.")

    while attempts > 0:
        print(f"\nCurrent word: {get_guessed_word(secret_word, letters_guessed)}")
        guess = input("Guess a letter: ").lower()

        # Check if the guess has already been made
        if guess in letters_guessed:
            print(f"You already guessed '{guess}'!")
        elif is_guess_in_word(guess, secret_word_ll):
            letters_guessed.append(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            letters_guessed.append(guess)
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

        # Check if the word has been completely guessed
        if is_word_guessed(secret_word_ll, letters_guessed):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break
    else:
        print(f"\nOut of attempts! The word was: {secret_word}")


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
