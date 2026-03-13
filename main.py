import MatrixMultiplication as mm
import numpy as np

def main():
    m1 = np.array([
        [9, 8, 1, 2],
        [0, 7, 2, 9],
        [6, 4, 3, 5],
        [5, 2, 8, 6]
    ])
    m2 = np.array([
        [8, 1, 4, 3],
        [2, 7, 7, 8],
        [3, 6, 4, 6],
        [1, 4, 7, 9],
    ])
    print(mm.MatrixMultiplier(m1, m2))

if __name__ == "__main__":
    main()