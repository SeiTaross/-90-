import numpy as np

H, W = map(int, input().split())

l_A = [list(map(int, input().split())) for _ in range(H)]

arr_A = np.array(l_A)

sum_column = np.sum(arr_A, axis=0)
sum_row = np.sum(arr_A, axis=1)


for i in range(H):
    for j in range(W): 
        print(sum_column[j] + sum_row[i] - l_A[i][j], end=" ")
    print()
