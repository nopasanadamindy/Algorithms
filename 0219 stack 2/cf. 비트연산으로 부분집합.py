
N = 3

data = [1, 2, 3]

for i in range(1 << N):
    for j in range(N + 1):
        if i & (1 << j):
            print(data[j], end = ' ')
    print()