#21343038
#AbelLevran
print("=========================================")
print(" ======== Gaussian Elimination ==========")
print("=========================================\n")
matrix = [[2, -1, -1],
    [4, 1, -1],
    [1, 1, 1]]

xyzA = [[1],
     [5],
     [0]]
print(matrix[0], xyzA[0])
print(matrix[1], xyzA[1])
print(matrix[2], xyzA[2])
print("\n")
def gaussian_elimination(A, b):
    n = len(A)
    # Append b as the last column of A
    for i in range(n):
        A[i].append(b[i])

    # Forward elimination
    for i in range(n - 1):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot_row][i]):
                pivot_row = j
        # Swap rows i and pivot_row
        A[i], A[pivot_row] = A[pivot_row], A[i]

        for j in range(i + 1, n):
            temp = A[j][i] / A[i][i]
            for k in range(i, n + 1):
                A[j][k] -= temp * A[i][k]

    # Backward substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x
A = [[2, -1, 1], [4, 1, -1], [1, 1, 1]]
b = [1, 5, 0]
x = gaussian_elimination(A, b)
print("[x,y,z] =",x)
