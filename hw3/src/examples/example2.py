import numpy as np

from matrix import Matrix2

if __name__ == '__main__':
    np.random.seed(0)

    m1 = Matrix2([])
    m2 = Matrix2([])

    m1.set_data(np.random.randint(0, 10, (10, 10)))
    m2.set_data(np.random.randint(0, 10, (10, 10)))

    addition_result = m1 + m2
    multiplication_result = m1 * m2
    matrix_multiplication_result = m1 @ m2

    addition_result.write_to_file("../../artifacts/2/matrix+.txt")
    multiplication_result.write_to_file("../../artifacts/2/matrix*.txt")
    matrix_multiplication_result.write_to_file("../../artifacts/2/matrix@.txt")
