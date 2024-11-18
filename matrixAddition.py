# Step 1: Define two matrices (same dimensions)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Step 2: Define a function to add the matrices
def add_matrices(m1, m2):
    # Step 3: Initialize an empty matrix for the result
    result = []
    
    # Step 4: Iterate through rows and columns to add corresponding elements
    for i in range(len(m1)):
        row = []  # Initialize an empty row
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])  # Add corresponding elements
        result.append(row)  # Add the row to the result matrix
    
    return result

# Step 5: Add the matrices and print the result
result_matrix = add_matrices(matrix1, matrix2)
print("Sum of the matrices:")
for row in result_matrix:
    print(row)
