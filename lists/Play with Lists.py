L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List: ", L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print("Sum = ", count)
print("Average =", avg)

L.sort()

print("Smallest Element Is: ", L[0])

print("The Largest ELement Is: ", L[-1])
