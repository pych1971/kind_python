def verify(matrix):
    res = True
    for i in range(len(matrix)):
        matrix[i].insert(0, 0)
        matrix[i].append(0)
    matrix.insert(0, [0] * len(matrix[0]))
    matrix.append([0] * len(matrix[0]))
    for i in range(1, len(matrix[0]) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j]:
                if not is_isolate(matrix, i, j):
                    return False
    return True


def is_isolate(matrix, i, j):
    sum = 0
    for i_i in range(i - 1, i + 2):
        for j_j in range(j - 1, j + 2):
            sum += matrix[i_i][j_j]
            if sum > 1:
                return False
    return True


matrix = []
matrix.append(list(map(int, input().split())))
for i in range(len(matrix[0]) - 1):
    matrix.append(list(map(int, input().split())))
print(verify(matrix))
