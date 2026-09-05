import random
playing = True
number = random.randint(0, 9)

print("I Will Generate A Number From 0 To 9, & You Have To Guess The Number, One Digit At A Time")
print("The Game Ends When You Get One Right! ")

while playing:
    guess = input("Give Me Your Best Guess! \n")
    if number == guess:
        print("You Won The Gane! ")
        print("The Number Was ", number)
        break

    else:
        print("Your Guess Isn't Quite Right, Try Again. \n")
        
        