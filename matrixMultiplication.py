# Step 1: Define two matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Step 2: Define a function to multiply two matrices
def multiply_matrices(m1, m2):
    # Step 3: Initialize an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    
    # Step 4: Perform matrix multiplication
    for i in range(len(m1)):  # Iterate through rows of matrix1
        for j in range(len(m2[0])):  # Iterate through columns of matrix2
            for k in range(len(m2)):  # Iterate through rows of matrix2
                result[i][j] += m1[i][k] * m2[k][j]  # Compute the dot product
                
    return result

# Step 5: Multiply the matrices and print the result
result_matrix = multiply_matrices(matrix1, matrix2)
print("Product of the matrices:")
for row in result_matrix:
    print(row)
