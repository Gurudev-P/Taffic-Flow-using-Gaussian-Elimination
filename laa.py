def gaussian_elimination(A):
    n = len(A)

    for i in range(n):
        pivot = A[i][i]

        if pivot == 0:
            print("Error: Zero pivot encountered!")
            return None

        for j in range(i, n+1):
            A[i][j] = A[i][j] / pivot

        for k in range(i+1, n):
            factor = A[k][i]
            for j in range(i, n+1):
                A[k][j] -= factor * A[i][j]

    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]

    return x


# INPUT
n = int(input("Enter number of intersections: "))

print("Enter total traffic flow at each intersection:")
b = []
for i in range(n):
    b.append(float(input(f"Intersection {i+1}: ")))


# MATRIX
A = []

for i in range(n):
    row = [0]*n

    if i < n-1:
        row[i] = 1
        row[i+1] = 1
    else:
        row[i] = 1   # breaks circular dependency

    row.append(b[i])
    A.append(row)


# SOLVE
solution = gaussian_elimination(A)

if solution:
    print("\nTraffic flows on roads:")
    for i, val in enumerate(solution):
        print(f"Road {i+1}: {val}")
