import numpy as np


class NumpyMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))

    def __str__(self):
        return str(self.data)

    @property
    def shape(self):
        return self.data.shape

    @property
    def dtype(self):
        return self.data.dtype

    @property
    def ndim(self):
        return self.data.ndim

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class HashMixin:
    def __hash__(self):
        return int(np.sum(self.data) % 100)
