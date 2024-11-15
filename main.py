import random
import hangman_assets as ha

lives = 6
placeholder = ""
chosen_word = random.choice(ha.word_list)
# print(chosen_word)
game_over = False
correct_letters = []
wrong_letters = []
for position in chosen_word:
    placeholder += "_"

print(ha.logo)

print(f"\nThe gallows have been prepared...\n{ha.stages[lives]}")

print(f"\nWord to guess -> \"{placeholder}\"   (each underscore is a letter)")

while not game_over:

    display = ""

    print(f"\n*************************** {lives}/6 LIVES LEFT ***************************")
    guess = input("\nGuess a letter: ").lower()

# display variable block
    for letter in chosen_word:
        if guess == letter:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

# correct and wrong letter list assignment block
    if guess in chosen_word:
        if guess not in correct_letters:
            correct_letters.append(guess)
            print(f"Good guess, the letter \"{guess}\", is in the word.")
        else:
            print(f"You've already guessed the letter \"{guess}\", try another letter.")
    else:
        if guess not in wrong_letters:
            wrong_letters.append(guess)
            lives -= 1
            print(f"\nYou guessed the letter \"{guess}\", that's not in the word. You lose a life.")
        else:
            print(f"You've already guessed the letter \"{guess}\", try another.")

    print(f"\nWord you're guessing: {display}\n")

# "lives broker" block
    if lives == 0:
        game_over = True
        print("***************************** YOU LOSE ********************************")
        print(f"                   THE WORD WAS \"{chosen_word}\"!")

    if "_" not in display:
        game_over = True
        print("***************************** YOU WIN ********************************")
        print(f"                   THE WORD WAS \"{chosen_word}\"!")

    print(ha.stages[lives])

# final message
print(f"You finished with {lives}/6 lives, your 'hangman' ^^^.\n", ha.stages[lives])
