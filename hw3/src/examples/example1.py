import numpy as np

from matrix import Matrix

if __name__ == '__main__':
    np.random.seed(0)
    matrix1 = np.random.randint(0, 10, (10, 10))
    matrix2 = np.random.randint(0, 10, (10, 10))

    m1 = Matrix(matrix1)
    m2 = Matrix(matrix2)

    addition_result = m1 + m2
    multiplication_result = m1 * m2
    matrix_multiplication_result = m1 @ m2

    with open("../../artifacts/1/matrix+.txt", "w") as file:
        file.write(str(addition_result.data))

    with open("../../artifacts/1/matrix*.txt", "w") as file:
        file.write(str(multiplication_result.data))

    with open("../../artifacts/1/matrix@.txt", "w") as file:
        file.write(str(matrix_multiplication_result.data))
