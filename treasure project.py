print("Welcome to treasure island\nYour mission is to find the treasure")
a=input("You have to cross the road type 'left' or 'right' ")
if a == "right":
    print("game over")
else:
    b=input("you come to a river chosse 'swim' or 'wait' for boat: ")
    if b=="swim":
        print("Game over")
    else:
        c=input("There are three gates choose one'yellow','red','blue' ")
        if c=="yellow":
            print("Game Over")
        elif c=="red":
            print("Game Over")
        else:
            print("You found the treasure")
    