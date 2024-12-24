# Input two digits, X and Y
X, Y = map(int, input("Enter two digits (X, Y): ").split(','))

# Initialize a 2D array filled with zeros
array = [[0 for j in range(Y)] for i in range(X)]

# Fill the array with values i * j
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j

# Print the 2D array
for row in array:
    print(row)