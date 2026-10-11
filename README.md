# Matrix Addition and Subtraction Using Python

## Aim

To write a Python program to perform addition and subtraction of two matrices using nested loops.

## Description

This program performs addition and subtraction on two 2×2 matrices using Python.

Two matrices, `m1` and `m2`, are defined with integer elements. Two result matrices are initialized with zeros. Using nested `for` loops, the program performs the following operations:

* **Matrix Addition:** Adds the corresponding elements of both matrices.
* **Matrix Subtraction:** Subtracts the corresponding elements of the second matrix from the first matrix.

Finally, the results are displayed row by row.

## Source Code

```python
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
```

## Sample Input

**Matrix 1:**

```text
1  2
3  4
```

**Matrix 2:**

```text
5  6
7  8
```

## Output

```text
Addition of matrices:
[6, 8]
[10, 12]
Subtraction of matrices:
[-4, -4]
[-4, -4]
```

## Concepts Used

* Python lists
* Two-dimensional matrices
* Nested `for` loops
* Matrix addition
* Matrix subtraction
* Indexing

## Applications

* Mathematical computations
* Scientific calculations
* Image processing
* Data manipulation
* Linear algebra operations

## Requirements

* Python 3.x
* Any Python IDE or code editor, such as IDLE, VS Code, or PyCharm.

## How to Run

1. Install Python 3 if it is not already installed.
2. Save the program as `matrix_operations.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the program.
5. Run the following command:

```bash
python matrix_operations.py
```

## Conclusion

The program successfully performs matrix addition and subtraction using nested loops. It demonstrates how corresponding elements of two matrices can be accessed and processed using Python.
