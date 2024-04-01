import numpy as np

from matrix import Matrix


if __name__ == '__main__':
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 0], [0, 1]])
    C = Matrix([[101, 102], [103, 104]])
    D = Matrix([[1, 0], [0, 1]])

    cache = {}

    AB = A @ B
    CD = C @ D

    path = "../../artifacts/3/"

    np.savetxt(path + 'A.txt', A.data, fmt='%d')
    np.savetxt(path + 'B.txt', B.data, fmt='%d')
    np.savetxt(path + 'C.txt', C.data, fmt='%d')
    np.savetxt(path + 'D.txt', D.data, fmt='%d')
    np.savetxt(path + 'AB.txt', AB.data, fmt='%d')
    np.savetxt(path + 'CD.txt', CD.data, fmt='%d')

    hash_AB = hash(AB)
    hash_CD = hash(CD)

    with open(path + 'hash.txt', 'w') as f:
        f.write(f'Hash AB: {hash_AB}\n')
        f.write(f'Hash CD: {hash_CD}')
