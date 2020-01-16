import sys


def toLetterGrade(number_grade):
    grade = "A"
    comment = "nice, lad"
    if (number_grade < 4):
        grade = "B"
        comment = "pretty good my dude"
    elif (number_grade <= 3):
        grade = "C"
        comment = ":("
    elif (number_grade <= 2):
        grade = "D"
        comment = ">:("
    else:
        grade = "F"
        comment = "No"
    return (grade, comment)


print(sys.argv[1])
print(toLetterGrade(int(sys.argv[1])))
print(sys.argv[2])
