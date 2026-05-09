print("Enter Marks Obtained In 5 Subjects:")

Mark1 = int(input())
Mark2 = int(input())
Mark3 = int(input())
Mark4 = int(input())
Mark5 = int(input())

Total = Mark1 + Mark2 + Mark3 + Mark4 + Mark5
Average = int(Total/5)

Valid_Range = range(0,101)

if Average not in Valid_Range:
    print("Invalid Input")

elif Average in range (91, 101):
    print("Your Grade IS A1")

elif Average in range (81, 91):
    print("Your Grade IS A2")

elif Average in range (71, 81):
    print("Your Grade IS B1")

elif Average in range (61, 71):
    print("Your Grade IS B2")

elif Average in range (51, 61):
    print("Your Grade IS C1")

elif Average in range (41, 51):
    print("Your Grade IS C2")

elif Average in range (33, 41):
    print("Your Grade IS D")

elif Average in range (21, 33):
    print("Your Grade IS E1")

elif Average in range (0, 21):
    print("Your Grade IS E2")