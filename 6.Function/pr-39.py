student = {}

print("\n========Student Report Card========")

student["name"] = input("Enter your name: ")
student["mark"] = float(input("Enter your mark: "))


print(f"Name : {student['name']}")
print(f"Mark : {student['mark']}")
for i in student:
    if student['mark'] >= 90:
        grade = "A"
    elif student['mark'] >= 80:
        grade = "B"
    elif student['mark'] >= 70:
        grade = "C"
    elif student['mark'] >= 60:
        grade = "D"
    else:
        grade = "F"

student["grade"] = grade

print(f"Grade : {student['grade']}")
print("================================")