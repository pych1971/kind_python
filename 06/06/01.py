grades = input().split()
d = {grade: grades[grade - int(grades[0]) + 1] for grade in range(int(grades[0]), int(grades[0]) + len(grades) - 1)}
print(d[4])
