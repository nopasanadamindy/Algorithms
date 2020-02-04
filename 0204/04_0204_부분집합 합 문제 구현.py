
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)

for i in range(1 << n):
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]

    if sum == 10:
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print()












# for i in range(1 << len(arr)):
#     sum = 0
#     for j in range(n):
#         if i & (1 << j):
#             sum += arr[j]
#     if sum == 10:
#         for j in range(n):
#             if i & (1 << j):
#                 print(arr[j], end = " ")
#         print()