import numpy as np


def mean_tanpa_library(data):
    if len(data) == 0:
        raise ValueError("Data tidak boleh kosong.")

    total = 0

    for nilai in data:
        total += nilai

    return total / len(data)


def mean_dengan_library(data):
    if len(data) == 0:
        raise ValueError("Data tidak boleh kosong.")

    return np.mean(data)


if __name__ == "__main__":
    data_latihan_1 = [80, 75, 90, 85, 70]
    data_latihan_2 = [10, 20, 30, 40, 50]

    print("Latihan 1:", mean_tanpa_library(data_latihan_1))
    print("Latihan 2:", mean_tanpa_library(data_latihan_2))
    print("Latihan 3:", mean_dengan_library(data_latihan_2))
