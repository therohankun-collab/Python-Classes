string = input("Please Enter Your Own Word: ")
char = input("Please Enter Your Own Character: ")
i = 0
count = 0
while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The total number of times", char, "has occurred is:", count)