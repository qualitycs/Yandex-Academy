import random

students = []
while True:
    try:
        name = input()
        students.append(name)
    except EOFError:
        break

random.shuffle(students)

for i in range(len(students)):
    student = students[i]
    secret_friend = students[(i + 1) % len(students)]
    print(f"{student} - {secret_friend}")
