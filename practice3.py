m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

array = [[0 for _ in range(n)] for _ in range(m)]

# Filling the array with some values (for example, using the row and column indices)
for i in range(m):
    for j in range(n):
        array[i][j] = i * n + j + 1

# Displaying the 2D array
for row in array:
    print(row)
