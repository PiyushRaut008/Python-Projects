import random
# two ways to import that
import word_list
from handman_art import stages
computer_choice = random.choice(word_list.word_list)
print(computer_choice)
lives = 6
from handman_art import logo
print(logo)
display = []
length = len(computer_choice)
for i in range(length):
    display += "_"
end = False
while not end:
    guess = input("choose a letter: ").lower()
    if guess in display:
        print(f"You already guess the letter{guess}")
    for position in range(length):
        letter = computer_choice[position]
        if letter == guess:
            display[position] = letter
    if guess not in computer_choice:
        print(f"The letter {guess} you guess is not in the word")
        lives -= 1
        if lives == 0:
            end = True
            print("You Loose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end = True
        print("You Win")
    print(stages[lives])