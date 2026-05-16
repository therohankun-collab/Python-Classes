print("Enter A Number (Numerator):")
numn = int(input())
print("Enter A Number (Denominator):")
numd = int(input())

if numn%numd == 0:
    print("\n" +str(numn)+ "Is Divisble By" +str(numd))
else:
    print("\n" +str(numn)+ "Is Not Divisble By" +str(numd))