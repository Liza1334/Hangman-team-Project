import random
HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")


MAX_WRONG = len(HANGMAN) - 1

WORDS = ("THE GRIND", "HANGMAN", "WHEEL OF FORTUNE",
         "AEROPOSTALE", "PYTHON", "CASABLANCA",
         "ALASKA", "SILLY GOOSE", "OVERUSED","sight", "crazy",
         "student","freeze","site", "summer", "winter", "avenue",
         "material", "dependence", "neighbor", "leeward", "providen", "maroon", "stop", "snake", "hello", "nice", "vibrant", "dog",
         "apple" ,"mango", "banana", "fruit", "laptop", "bottle", "curtain", "college", "class", "secret", "friend", "light", "mirror", "umbrella",
         "uniform", "vehicle", "professor", "chancellor", "india" ,"country", "future", "invest", "love", "jackpot", "fish", "dark", "goofy", "chuckle")

word = random.choice(WORDS)

so_far = "-" * len(word) 

wrong = 0 

used = []

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ("\nYou've used the following letters:\n", used)
    print ("\nSo far, you have guessed:\t", so_far)

    guess = input("Enter your guess:\t")
    guess = guess.upper()

    while guess in used:
        print ("You already guessed the letter:\t", guess)
        guess = input("Guess again:\t")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print ("The letter, ", guess, "is in the word")

        new = ""


        for i in range(len(word)):
            if guess == word [i]:
                new += guess
            else:
                new += so_far [i]
        so_far = new

    else:
        print ("\nSorry,", guess, "isn't in word")
        wrong += 1

if wrong == MAX_WRONG:
    print (HANGMAN[WRONG])
    print ("I would tell you, that you've been hanged. \n\
But you're dead, so.......RIP?")

else:
    print("\nYou guessed it!")

print("\nThe word was", word)

input ("\n\nPress Enter key to exit")
