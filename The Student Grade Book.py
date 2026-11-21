grades = {
    "Alice": 92,
    "Ben": 78,
    "Chloe": 85,
    "David": 96,
    "Emma": 71
}


total = 0
for score in grades.values():
    total += score

average = total / len(grades)
print("Class average:", average)

top_name = ""
bottom_name = ""
top_score = -1
bottom_score = 101

for name, score in grades.items():
    if score > top_score:
        top_name = name
        top_score = score

    if score < bottom_score:
        bottom_name = name
        bottom_score = score

print("Top scorer:", top_name, "-", top_score)
print("Bottom scorer:", bottom_name, "-", bottom_score)

name = input("Enter a student name: ").strip()
score = grades.get(name)

if score is None:
    print("Student not found.")
else:
    print(name + "'s score:", score)