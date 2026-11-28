grades={
    "Alice": 92,
    "Ben": 78,
    "Chloe": 85,
    "David": 96,
    "Emma": 71
}

total = 0

for score in grades.values():
    total += score

average = total/len(grades)
print("Class Average: ", average)

top_name = ""
bottom_name=""  

top_score = -1
bottom_score = 101

for name, score in grades.items():
    if score > top_score:
        top_name = name
        top_score = score
    if score < bottom_score:
        bottom_name = name
        bottom_score = score

print("Top Scorer: ", top_name, "W/ Score: ", top_score)
print("Bottom Scorer: ", bottom_name, "W/ Score: ", bottom_score)

check = input("Do you Want To See The Scores Of The Students? (Y/N): ").strip().lower()
if check == "y":
    ask=input("Which student's score would you like to see?" ).strip()
    score = grades.get(ask)
    if score is None:
        print("Student not found.")
    else:
        print(ask + "'s score is: ", score)
elif check == "n":
    print("Thank You For Using The Program!")

