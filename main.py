import random

import hangman_assets

lives = 6

print(hangman_assets.logo)

chosen_word = random.choice(hangman_assets.word_list)
# print(chosen_word)

placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(hangman_assets.stages[lives])
print("\nWord to guess -> " + placeholder + "   (each underscore is a letter)")

game_over = False
correct_letters = []

while not game_over:

    print(f"\n*************************** {lives}/6 LIVES LEFT ***************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess in correct_letters:
                print(f"You've already guessed {guess}")
            else:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("\nWord to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed the letter \"{guess}\", that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print("***************************** YOU LOSE ********************************")
            print(f"                   THE WORD WAS {chosen_word}!")

    if "_" not in display:
        game_over = True
        print("***************************** YOU WIN ********************************")
        print(f"                   THE WORD WAS {chosen_word}!")

    print(f"You finished with {lives}/6, your 'hangman' below:\n", hangman_assets.stages[lives])
  
