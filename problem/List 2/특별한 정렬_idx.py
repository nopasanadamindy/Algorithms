def sorting(data):
    x = data[i-1]
    for i in range(1, len(data)+1):
        if data[i] <= x:
            x, data[i] = data[i], x
        else:
            x, data[i] = x, data[i]
    return data


import sys
sys.stdin = open('특별한 정렬.txt')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    data = list(map(int, input().split()))
    print(sorting(data))