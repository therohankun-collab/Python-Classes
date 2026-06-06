string = input("Please Enter Your Own String: ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\n The Original String Is: ", string)
print("\nThe Reversed String Is: ", string2)