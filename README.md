# NumPy Matrix Calculator

A command-line matrix calculator developed in Python using NumPy. The project performs common matrix operations while applying basic linear algebra rules and input validation.

## Features

- Matrix addition
- Matrix subtraction
- Matrix multiplication
- Matrix transpose
- Matrix determinant
- Matrix inverse
- Interactive command-line menu
- Matrix dimension validation
- Handling of singular matrices

## Technologies

- Python 3
- NumPy
- NumPy Linear Algebra (`numpy.linalg`)

## Operations

### Matrix Addition
Adds two matrices with matching dimensions.

### Matrix Subtraction
Subtracts one matrix from another when both matrices have the same dimensions.

### Matrix Multiplication
Performs standard matrix multiplication using the `@` operator.

The number of columns in Matrix A must equal the number of rows in Matrix B.

### Matrix Transpose
Converts rows into columns using NumPy's `.T` attribute.

### Determinant
Calculates the determinant of a square matrix using `numpy.linalg.det()`.

### Matrix Inverse
Calculates the inverse of a square, non-singular matrix using `numpy.linalg.inv()`.

Singular matrices are handled using exception handling.

## Project Structure

```text
numpy-matrix-calculator/
│
├── matrix_calculator.py
├── README.md
├── requirements.txt
└── .gitignore
