import random


def the_words():
    word = ["cat", "dog", "dragon", "Pineapple", "seahorse", "gladiator", "crocodile", "ferrari", "waterfall", "butterfly", "jazz", "squirrel", "porcupine"]
    word_random = word[random.randint(0, 12)]
    return word_random


def game(word):
    word_line = "*" * len(word)                                        # variable to show how long the word is
    guessedsofar = False
    guessedsofar_letters = []                                          # list that holds the letters, the user guessed
    guessedsofar_words = []                                            # list that holds the words, the user guessed
    tries = 6                                                          # 6 tries, due to 6 bodyparts (head, body, both arms and both legs)
    print("Welcome to Hangman!")                                       # starting out printing these things
    print("Let's see if you can guess the word!")
    print(display_hangman(tries))
    print("your word is: ", word_line)
    print("\n")
    while not guessedsofar and tries > 0:                              # loop that will continue until the word is guessed or out of tries
        guess = input("Enter a letter or a word: ")          # asks user for a guess
        if len(guess) == 1 and guess.isalpha():                        # the guess has a length of 1 and is from the alphabet
            if guess in guessedsofar_letters:                          # if the letter is already guessed
                print("You already guessed this letter", guess)
            elif guess not in word:                                    # if guess is not in the word
                print(guess, "is not in the word.")
                tries -= 1                                             # it takes 1 try away from the starting 6
                guessedsofar_letters.append(guess)                     # Append guess to guessed letters
            else:
                print("Nice! ", guess, "is in the word!")              # print, if the guess is correct
                guessedsofar_letters.append(guess)
                word_as_list = list(word_line)                         # adding the guess to the underscores
                indices = [i for i, letter in enumerate(word) if letter == guess]         # calling an enumerate to get both the index i and letter at index for each iteration
                for index in indices:                                  # making a for loop, to replace the underscores with guess
                    word_as_list[index] = guess
                word_line = "".join(word_as_list)
                if "*" not in word_line:                               # if the guess is true, the underscore will be removed
                    guessedsofar = True
        elif len(guess) == len(word) and guess.isalpha():              # if the length of the guess and word is the same and it is alphabetic
            if guess in guessedsofar_words:                            # if the guess is already guessed
                print("You already guessed the word", guess)
            elif guess != word:                                        # if the guess is not the word
                print("Wrong ", guess, "is not the correct word.")
                tries -= 1
                guessedsofar_words.append(guess)
            else:
                guessedsofar = True                                    # else the guess is true
                word_line = word                                       # the word will be written on the underscores
        else:
            print("incorrect!")
        print(display_hangman(tries))
        print(word_line)
        print("\n")
    if guessedsofar:
        print("Congrats, you guessed the word! You are a winner!")
    else:
        print("unfortunately, you ran out of tries. The word was " + word + ". Maybe next time loser!")


def display_hangman(tries):
    stages = [  # the whole hangman
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, body, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, body, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, body, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and body
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # the noose
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = the_words()
    game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = the_words()
        game(word)


if __name__ == "__main__":
    main()
