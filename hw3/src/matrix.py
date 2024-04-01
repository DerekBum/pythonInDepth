import numpy as np

from mixins import NumpyMixin, HashMixin


class Matrix(HashMixin):
    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices dimensions are incorrect for addition.")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices dimensions are incorrect for multiplication.")
            return Matrix(np.multiply(self.data, other.data))
        else:
            return Matrix(self.data * other)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Matrices dimensions are incorrect for multiplication.")
        return Matrix(np.matmul(self.data, other.data))

    def __str__(self):
        return str(self.data)


class Matrix2(NumpyMixin):
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        return Matrix2(self.data + other.data)

    def __sub__(self, other):
        return Matrix2(self.data - other.data)

    def __mul__(self, other):
        return Matrix2(self.data * other.data)

    def __matmul__(self, other):
        return Matrix2(self.data @ other.data)

    def __truediv__(self, other):
        return Matrix2(self.data / other.data)
