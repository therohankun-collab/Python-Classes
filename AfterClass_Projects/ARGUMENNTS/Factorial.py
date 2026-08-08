def factorial(x):
 if x==0 or x==1:
    return 1
 else:
   return x*factorial(x-1)

print("The Factorial Of 0: ", factorial(0))
print("The Factorial Of 1: ", factorial(1))
print("The Factorial Of 2: ", factorial(2))
print("The Factorial Of 5: ", factorial(5))
print("The Factorial Of 10: ", factorial(10))