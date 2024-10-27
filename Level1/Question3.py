a = []
marks = {}
print("Enter in the marks in order: Physics , Chemestry, Biology , Mathematics and Computer")
for i in range(0,5):
    n = int(input("Enter the marks"))
    a.append(n)
for i in a:
    if i >= 90:
        marks[i] = "A"
    elif i>=80 and i < 90:
        marks[i] = "B"
    elif i>=70 and i<80:
        marks[i] ="C"
    elif i>=60 and i<70:
        marks[i] = "D"
    elif i>=40 and i<60:
        marks[i] = "E"
    else:
        marks[i] = "F"

print(marks)