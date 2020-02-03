
# 부분집합 합이 10이 되는 것이 존재하는 지를 계산하는 함수를 작성해보자

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(arr)

for i in range(1 << n): # 1 << n : 부분집합의 갯수
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = '')

    print()

for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]

    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print()