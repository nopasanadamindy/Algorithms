arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)

for i in range(3):
    for j in range(i + 1, len(arr[i])):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)