import numpy as np


def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print(f"Enter {rows} rows (space-separated values):")

    for i in range(rows):
        while True:
            row_input = input(f"Row {i + 1}: ").split()

            if len(row_input) != cols:
                print(f"Expected {cols} values. Try again.")
                continue

            try:
                row = [float(value) for value in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid numbers.")

    return np.array(matrix)


def add_matrices():
    print("\n--- Matrix Addition ---")
    print("Matrix A:")
    matrix_a = input_matrix()

    print("\nMatrix B:")
    matrix_b = input_matrix()

    if matrix_a.shape != matrix_b.shape:
        print(
            f"\n❌ Cannot add matrices with shapes {matrix_a.shape} and {matrix_b.shape}."
        )
        return

    result = matrix_a + matrix_b
    print("\nResult (A + B):")
    print(result)


def subtract_matrices():
    print("\n--- Matrix Subtraction ---")
    print("Matrix A:")
    matrix_a = input_matrix()

    print("\nMatrix B:")
    matrix_b = input_matrix()

    if matrix_a.shape != matrix_b.shape:
        print(
            f"\n❌ Cannot subtract matrices with shapes {matrix_a.shape} and {matrix_b.shape}."
        )
        return

    result = matrix_a - matrix_b
    print("\nResult (A - B):")
    print(result)


def multiply_matrices():
    print("\n--- Matrix Multiplication ---")
    print("Matrix A:")
    matrix_a = input_matrix()

    print("\nMatrix B:")
    matrix_b = input_matrix()

    if matrix_a.shape[1] != matrix_b.shape[0]:
        print(
            f"\n❌ Cannot multiply matrices: Columns of A ({matrix_a.shape[1]}) "
            f"must match Rows of B ({matrix_b.shape[0]})."
        )
        return

    result = matrix_a @ matrix_b
    print("\nResult (A @ B):")
    print(result)


def transpose_matrix():
    print("\n--- Matrix Transpose ---")
    matrix = input_matrix()
    result = matrix.T

    print("\nOriginal Matrix:")
    print(matrix)
    print("\nTranspose (Aᵀ):")
    print(result)


def determinant_matrix():
    print("\n--- Matrix Determinant ---")
    matrix = input_matrix()

    if matrix.shape[0] != matrix.shape[1]:
        print(
            f"\n❌ Cannot calculate determinant: Matrix is {matrix.shape[0]}x{matrix.shape[1]}. "
            "Must be a square matrix!"
        )
        return

    det = np.linalg.det(matrix)
    print("\nMatrix:")
    print(matrix)
    print(f"\nDeterminant: {det:.2f}")


def inverse_matrix():
    print("\n--- Matrix Inverse ---")
    matrix = input_matrix()

    if matrix.shape[0] != matrix.shape[1]:
        print(
            f"\n❌ Cannot calculate inverse: Matrix is {matrix.shape[0]}x{matrix.shape[1]}. "
            "Must be a square matrix!"
        )
        return

    try:
        inverse = np.linalg.inv(matrix)
        print("\nOriginal Matrix:")
        print(matrix)
        print("\nInverse (A⁻¹):")
        print(inverse)
    except np.linalg.LinAlgError:
        print("\n❌ Error: Matrix is singular (determinant is 0) and has no inverse.")


def main():
    while True:
        print("\n" + "=" * 10 + " NumPy Matrix Calculator " + "=" * 10)
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant")
        print("6. Inverse")
        print("7. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_matrices()
        elif choice == "2":
            subtract_matrices()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            determinant_matrix()
        elif choice == "6":
            inverse_matrix()
        elif choice == "7":
            print("\nThank you for using the Matrix Calculator. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()