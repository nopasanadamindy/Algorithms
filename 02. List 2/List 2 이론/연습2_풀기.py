# data = [-7, -3, -2, 5, 8]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = len(data)

for i in range(1<<N):
    sum = 0
    for j in range(N):
        if i & (1 << j):
            sum += data[j]
    # print(sum)
    if sum == 10:
        for j in range(N): ###
            if i & (1<<j):
                print(data[j], end = ' ')
        print()