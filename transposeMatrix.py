# Step 1: Define a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Step 2: Define a function to transpose the matrix
def transpose_matrix(m):
    # Step 3: Use list comprehension to transpose the matrix
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Step 4: Transpose the matrix and print the result
transposed = transpose_matrix(matrix)
print("Transposed matrix:")
for row in transposed:
    print(row)
