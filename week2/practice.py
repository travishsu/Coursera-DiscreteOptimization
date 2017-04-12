import numpy as np

K = 7
N = 4

v = np.array([0, 16, 19, 23, 28])
w = np.array([0, 2, 3, 4, 5])

O = np.zeros((K+1, N+1), dtype=int)

for _ in range(N):
    for __ in range(K):
        j = _  + 1
        i = __ + 1
        if w[j] <= i:
            O[i, j] = max(O[i, j-1], v[j] + O[i-w[j], j-1])
        else:
            O[i, j] = O[i, j-1]

        # print("({} {}): {}".format(i, j, O[i, j]))

print(O)
