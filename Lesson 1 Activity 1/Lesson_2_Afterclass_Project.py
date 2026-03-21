# Raj Has Five Friends
print("Raj Has Five Friends")
print("Their Names Are Bella, Daksh, Ayush, Aarav & Suzie")

# We add .lower() at the end of the input to convert "BeLla" to "bella"
name = input("Please Enter Whose Birth Date You Want To Know: ").lower()

# Now you only need to check against the lowercase version!
if name == "bella":
    print("Bella Is A Girl, 11 years Old, And Her Birthday Is On 21 April")

elif name == "daksh":
    print("Daksh Is A Boy, 12 years Old, And His Birthday Is On 28 May")

elif name == "ayush":
    print("Ayush Is A Boy, 11 years Old, And His Birthday Is On 15 March")

elif name == "aarav":
    print("Aarav Is A Boy, 10 years Old, And His Birthday Is On 21 April")

elif name == "suzie":
    print("Suzie Is A Girl, 12 years Old, And Her Birthday Is On 21 April")

else:
    print("Sorry, that name isn't in Raj's friend list!")


