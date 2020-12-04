import random
import os
import hangman_art
import hangman_words

print(hangman_art.Logo)
display = []
lives = 6
stages_reversed = 6
clear = lambda: os.system('cls')
game_state = True

chosen_word = random.choice(hangman_words.word_list)

for dash in chosen_word:
    display.append("-")


while game_state == True:
    guess = input("Guess a letter from the word: ").lower()
    clear()
    if guess in display:
        print(f"You have already chosen the letter {guess}")

    for letter in range(0, len(chosen_word)):

        if guess == chosen_word[letter]:
            display[letter] = guess



    if guess not in chosen_word:
        lives -=1
        print(f"\nThe letter {guess} is not in the word")
        print(f"You now have {lives} lives left")
        print(hangman_art.stages[stages_reversed])
        stages_reversed -=1


    if "-" not in display:
        print(display)
        print("You won")
        break
    if lives == 0:
        print(display)
        print(f"\nThe letter {guess} is not in the word")
        print(f"You now have {lives} lives left")
        print("You Lose")
        break
    print(display)


print('\n' + "The word is: " + chosen_word)

