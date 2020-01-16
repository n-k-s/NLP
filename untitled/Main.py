print("im an expert at python :^)");

print("Hello world")
gpas = [3.5, 3.4, 2.7, 4.0, 3.3]
sum = 0
for x in gpas:
    sum += x
avg = sum / len(gpas)
print("Average is " + str(avg))
grade = "A"
comment = "nice, lad"
if (avg < 4):
    grade = "B"
    comment = "pretty good my dude"
elif (avg < 3):
    grade = "C"
    comment = ":("
elif (avg < 2):
    grade = "D"
    comment = ">:("
else:
    grade = "F"
    comment = "No"
print(grade + "\n" + comment)


def average(elements):
    sum = 0
    for x in elements:
        sum += x
    return sum / len(elements)


def toLetterGrade(numGrade):
    grade = "A"
    comment = "nice, lad"
    if (numGrade < 4):
        grade = "B"
        comment = "pretty good my dude"
    elif (numGrade < 3):
        grade = "C"
        comment = ":("
    elif (numGrade < 2):
        grade = "D"
        comment = ">:("
    else:
        grade = "F"
        comment = "No"
    return (grade, comment)


avg = average(gpas)
print("the average is " + str(average(gpas)))

lGrade, com = toLetterGrade(avg)

print(lGrade + "\n" + com)

# dictionaries
grades = {"Frank": 3.2, "Jane": 3.7, "Martha": 3.7, "Simon": 1.2, "Billy": 4.0}
grades["Ginger"] = 1000000.1;
print(grades['Billy'])
grades["Simon"] = 3.2
print(grades)

import sys

print(sys.argv[1])
#print(toLetterGrade(int(sys.argv[1])))
