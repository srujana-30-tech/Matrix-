    # Define two matrices
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

# Initialize matrices for the results
addition_result = [[0, 0], [0, 0]]
subtraction_result = [[0, 0], [0, 0]]

# Perform addition and subtraction
for i in range(len(m1)):
    for j in range(len(m1[0])):
        addition_result[i][j] = m1[i][j] + m2[i][j]
        subtraction_result[i][j] = m1[i][j] - m2[i][j]

# Print the results
print("Addition of matrices:")
for row in addition_result:
    print(row)

print("Subtraction of matrices:")
for row in subtraction_result:
    print(row)
