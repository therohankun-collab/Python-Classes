# Added this line to prevent the crash
temp2 = "" 

temperature = float(input("Enter Temperature: "))

clothes = "Light Clothes"
clothes_1 = "Heavy Clothes"
clothes_2 = "Medium, Lightweight Clothes"

temp1 = input("Celsius Or Farenheit? ")

if temp1 == "Celsius" or temp1 == "celsius" or temp1 == "CELSIUS" or temp1 == "C" or temp1 == "c":
    temp2 = input("Celsius? ")
    if temp2 == "Yes" or temp2 == "yes" or temp2 == "YES" or temp2 == "yEs":
        if temperature > 18 and temperature < 20:
            print("Wear", clothes_1)
        elif temperature > 21 and temperature < 26:
            print("Wear", clothes_2)
        elif temperature > 26:
            print("Wear", clothes)

elif temp1 == "Farenheit" or temp1 == "farenheit" or temp1 == "FARENHEIT" or temp1 == "F" or temp1 == "f":
    temp3 = input("Farenheit? ")
    if temp3 == "Yes" or temp3 == "yes" or temp3 == "YES" or temp3 == "yEs":
        if temperature > 64 and temperature < 68:
            print("Wear", clothes_1)
        elif temperature > 69 and temperature < 78:
            print("Wear", clothes_2)
        elif temperature > 78:
            print("Wear", clothes)

if temp2 == "no" or temp2 == "NO" or temp2 == "No" or temp2 == "nO":
    trk4 = input("Farenheit? ")
    if trk4 == "Yes" or trk4 == "yes" or trk4 == "YES" or trk4 == "yEs":
        if temperature > 64 and temperature < 68:
            print("Wear", clothes_1)
        elif temperature > 69 and temperature < 78:
            print("Wear", clothes_2)
        elif temperature > 78:
            print("Wear", clothes)