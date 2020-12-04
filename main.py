import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["adri","fatty","love"]
display = []
lives = 6
stages_reversed = 6

game_state = True

chosen_word = random.choice(word_list)

for dash in chosen_word:
    display.append("-")


while game_state == True:
    guess = input("Guess a letter from the word: ").lower()

    for letter in range(0, len(chosen_word)):

        if guess == chosen_word[letter]:
            display[letter] = guess

    if guess not in chosen_word:
        lives -=1
        print(stages[stages_reversed])
        stages_reversed -=1


    if "-" not in display:
        print(display)
        print("You won")
        break
    if lives == 0:
        print(display)
        print("You Lose")
        break
    print(display)


print('\n' + "The word is: " + chosen_word)

