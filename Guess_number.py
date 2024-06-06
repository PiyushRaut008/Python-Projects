#17 Guess the number game
import random
def function():
    def call(num):
        for i in range(1, num):
            if i == num - 1:
                print("You lost")
                break
            print(f"You have {(num - 1) - i} attempts left to guess the number")
            c = int(input("Make a Guess: "))
            if c > b:
                print("Number is too high")
            elif c < b:
                print("Number is too Low")
            elif c == b:
                print("Congratulation! You make the correct Guess")
                break
    print("Hello Noobs welcome to the Game Guess the Number")
    print("I am thinking of a number between 1 to 100")
    b = random.randint(1, 100)
    a = input("Choose the difficulty level: Type 1 for easy and Type 2 for difficult: ")
    if int(a) == 1:
        call(12)
    elif int(a) == 2:
        call(7)
    else:
        print("Enter 1 or 2 only")
        print(" ")
        function()
function()
