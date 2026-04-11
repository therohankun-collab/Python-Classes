print ("Enter Marks Scored In 4 Subjects")
Math = int (input ("Maths:"))
English = int (input ("English:"))
Science = int (input ("Science:"))
Hindi = int (input ("Hindi:"))

sum = Math + English + Science + Hindi
print ("Sum Of Math, Science, English & Hindi is:", sum)

perc= (sum/400)*100

print (end= "Percentage Marks:")
print (perc)