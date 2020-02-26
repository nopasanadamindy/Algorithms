def sorting(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
import sys
sys.stdin = open('특별한정렬_input.txt')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    data = list(map(int, input().split()))
    # print(data)
    sorting(data)
    result = []
    maxi = len(data) - 1
    mini = 0
    cnt = 0
    while cnt < 5:
        result.append(data[maxi])
        result.append(data[mini])
        maxi -= 1
        mini += 1
        cnt += 1
    print('#{}'.format(test_case), end = ' ')
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()