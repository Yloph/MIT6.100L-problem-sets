# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


def help_mode( secret_word , available_letters ):
    '''
    secret_word: string,the lowercase word that user is guessing
    available_letters: string,the alpha that have not been guessed

    returns: a letter that are both in secret_word and available_letters
    '''
    choose_from = []
    for e in secret_word:

        if e in available_letters:

            choose_from.append( e )

    choose_from = ''.join( choose_from )
    choose_index = random.randint( 0 , len( choose_from ) - 1 ) 
    reveal_letter = choose_from[ choose_index ]

    return reveal_letter  


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    if len( letters_guessed ) == 0:
        
        return False
    
    else:
        
        to_list = list( secret_word )
        for e in to_list:
            
            if e not in letters_guessed:
                
                return False
            
        return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    res = ""
    to_list = list( secret_word )
    for e in to_list:
        
        if e in letters_guessed:
            
            res = res + e
        
        else:
            
            res = res + '*'

    return res


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    
    available_letters = string.ascii_lowercase
    to_list = list( available_letters )
    for e in letters_guessed:
        
        if e in to_list:
            
            to_list.remove( e )

    available_letters = ''.join( to_list )

    return available_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    ## game setup
    print("Welcome to Hangman!")
    
    word_len = len(secret_word)
    print(f'I am thinking of a word that is {word_len} letters long.')

    ## user-computer interaction
    guess = 10
    letters_guessed = []
    guessing_word = get_word_progress( secret_word , letters_guessed )
    win = False
    while guess > 0 and not win:
        
        # print 3 dashes,guess and available letters every round
        available_letters = get_available_letters( letters_guessed )
        print("--------------")
        print(f"You have { guess } guesses left.")
        print("Available letters:",available_letters)

        # user input
        letter_in = input("Please guess a letter: ")

        # react for user input
        letter_len = len( letter_in )
        # check single
        if letter_len != 1:

            guessing_word = get_word_progress( secret_word , letters_guessed )
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",guessing_word)

        else:

            # check game with help
            if with_help == True and letter_in == '!':

                if guess > 3:

                    revealed_letter = help_mode( secret_word , available_letters )
                    letters_guessed.append( revealed_letter )
                    print("Letter revealed:",revealed_letter)
                    guessing_word = get_word_progress( secret_word , letters_guessed )
                    print(guessing_word)                
                    guess = guess - 3

                else:
                    
                    guessing_word = get_word_progress( secret_word , letters_guessed )
                    print("Oops! Not enough guesses left:",guessing_word)

            # check alpha
            elif letter_in.isalpha():
                
                letters_guessed.append( letter_in.lower() )

                # guess right
                if letter_in not in secret_word:
                    
                    # consonant or vowel
                    if letter_in in "aeiou":
                        
                        if guess == 1:
                            
                            break
                        
                        guess = guess - 2

                    else:
                        
                        guess = guess - 1
                    
                    guessing_word = get_word_progress( secret_word , letters_guessed )
                    print("Oops! That letter is not in my word:",guessing_word)

                elif letter_in in guessing_word:
                    
                    guessing_word = get_word_progress( secret_word , letters_guessed )
                    print("Oops! You've already guessed that letter:",guessing_word)

                else:
                    
                    guessing_word = get_word_progress( secret_word , letters_guessed )
                    print("Good guess:",guessing_word)
            
            # not game with help or alpha
            else:

                guessing_word = get_word_progress( secret_word , letters_guessed )
                print("Oops! That is not a valid letter. Please input a letter from the alphabet:",guessing_word)

            # whether win
            win = has_player_won( secret_word , letters_guessed )

    print("--------------")
    if not win:
        
        print("Sorry, you ran out of guesses. The word was",secret_word)

    else:
        
        print("Congratulations, you won!")
        # calculate the score
        unique_letter = []
        for e in secret_word:
            
            if e not in unique_letter:
                
                unique_letter.append( e )

        total_score = guess + 4 * len( unique_letter ) + 3 * len( secret_word )
        print("Your total score for this game is:",total_score)
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

