Amount = int(input("Please Enter The Amount That You Want to Withdraw:"))

note_1= Amount//100
note_2= (Amount%100)//50
note_3= ((Amount%100)%50)//10

print ("Notes Of 100 Rupees is:", note_1)
print ("Notes Of 50 Rupees is:", note_2)
print ("Notes Of 10 Rupees is:", note_3)
