# -*- coding: utf-8 -*-


import random
import time

print("\nWelcome to Hangman\n")
name = input("Enter your name: ")
print("Hi " + name + "! Good luck! (you'll need it ;p )")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

  

def main():
    global count
    global display
    global notsplitDisplay
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["pencil","border","ball","film","beautiful","camera","vine","zebra","light","glass","bottle"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    notsplitDisplay = '-' * length
    display= split(notsplitDisplay)
    already_guessed = []
    play_game = ""
    
def split(word): 
    return list(word)   
    

        
def play_loop():
    global play_game
    play_game= input("Do you want to play again? y = yes, n = no \n")
    play_game= play_game.lower()
    if play_game == "y"or play_game == "yes":
        main()
        hangman()
    elif play_game == "n" or play_game == "no":
        print("Thanks For Playing! See you soon!")
        raise SystemExit
    else:
        print("I'm sorry, I did not understand.")
        play_loop()
        

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global str1
    global str2
    str1=""
    str2=""
    limit = 6
    guess = input("This is the Hangman Word: " + str1.join(display) + " Enter your guess: \n")
    guess= guess.lower()
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in set(word):
        display = [guess if letter == guess else display for display, letter in zip(display, word)]
        print(str1.join(display))
        already_guessed.append(guess)


    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1
        already_guessed.append(guess)

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |       you guessed:" + str2.join(already_guessed)+"\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |       you guessed:"+ str2.join(already_guessed)+"\n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     |      you guessed:" + str2.join(already_guessed)+"\n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |    \| \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |       you guessed:"+ str2.join(already_guessed)+"\n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    \|/ \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |       you guessed:"+ str2.join(already_guessed)+"\n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    \|/ \n"
                  "  |    / \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")


        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |"+ str2.join(already_guessed)+"\n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",word)
            play_loop()

    if word == str1.join(display):
        print("Congrats! You have guessed the word! (I'm actually surprised!) ")
        print(word)
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()
        
        
        