
file = open("Mini Project - Marks Adding.csv", "r")
data = file.readlines()
file.close()

roll_marks = {}

for line in data:
    roll, marks = line.strip().split(" ")
    if roll in roll_marks:
        roll_marks[roll] += int(marks)
    else:
        roll_marks[roll] = int(marks)

file1 = open("Mini Project - Marks Adding.csv", "w")


for roll, marks in roll_marks.items():
    file1.write(f"{roll} {marks}\n")


file1.close()
