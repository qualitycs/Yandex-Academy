approvedStudents = []
students = []
n = int(input())
for i in range(n):
    student = input()
    students.append(student)
    a = list(student)
    if int(a[-1]) >= 4:
        approvedStudents.append(student)
print(*students, sep='\n')
print('\n', end='')
print(*approvedStudents, sep='\n')
