# Hangman-Team-Project
This repository contains the source code for The Hangman game team project and related file for a simpler description of the game , the logic behind its implementation, and instruction for running the game.
In this game the word to guess is represented by a row of dashes representing each letter or number of the word. Rules may permit or forbid proper nouns, such as names, places, brands, or slang. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions. If the suggested letter does not occur in the word, the other player adds (or alternatively, removes) one element of a hanged stick figure as a tally mark. Generally, the game ends once the word is guessed, or if the stick figure is complete — signifying that all guesses have been used.
The player guessing the word may, at any time, attempt to guess the whole word. If the word is correct, the game is over and the guesser wins. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. If the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed.

# NAME OF TEAM -- TRISTAR INNOVATIONS
MANAGER -- LIZA GARG
DEVELOPER -- JIYA MEHTA
TESTER -- ISHITA

# VERSION 1
~ As the game starts, it welcomes the user.
~ It asks you to enter an Alphabet of the random word .
~ If you enter the correct word, it prints " The Letter, {} is in the word."
~ If the alphabet is not in the word, it prints "Sorry, {} isn't in word."
~ Once you guess the correct word it prints, "You guessed it!."

~ If you enter invalid input (number), it still considers it an alphabet 
~ It you enter any character , it stops the game .

# VERSION 2
~ The game starts with welcoming the user.
~ You have total 10 attempts to guess the word.
~ If you enter an alphabet which is in the random word , it doesn't count as an attempt .
~ If you enter wrong alphabet, it reduces one attempt and the length of Hangman is increased .
~ If you enter an alphabet or any special character (which is not correct input), it prints "That is not a letter . Please try again." and it does not count as an attempt .
~ If you guess the word correctly after yoyur 10 attempts , it prints "Congratulations! {} was the word."
~ If you fail to guess the word after your attempts, it prints "Umlucky! The word was {}." and tells the correct word.
~ It also asks if you want to play the game again .
~ If yes, enter "y" to say yes and you can play the game again .
~ At the end, if you gues the word correctly you save the Hangman. Otherwise the game concludes.
