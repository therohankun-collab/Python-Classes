num = int(input("Enter A Number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "Is An Armstrong Number")
else:
    print(num, "Is Not An Armstrong Number")