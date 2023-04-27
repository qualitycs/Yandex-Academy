number_of_classes = int(input())
classes_have_excellent_students = []

for _ in range(number_of_classes):
    number_of_students = int(input())
    students_grades = []

    for _ in range(number_of_students):
        student, grade = input().split()
        students_grades.append(int(grade))

    classes_have_excellent_students.append(any(grade == 5 for grade in students_grades))

if all(classes_have_excellent_students):
    print("ДА")
else:
    print("НЕТ")
