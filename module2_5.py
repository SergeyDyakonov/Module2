def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
r1 = get_matrix(1, 2, 4)
r2 = get_matrix(3,3,5)
r2 = get_matrix(5,5,1)
