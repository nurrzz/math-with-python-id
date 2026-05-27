import numpy as np


def mean(data):
    if len(data) == 0:
        raise ValueError("Data tidak boleh kosong.")

    return np.mean(data)


if __name__ == "__main__":
    nilai_ujian = [70, 80, 90]
    print(mean(nilai_ujian))
