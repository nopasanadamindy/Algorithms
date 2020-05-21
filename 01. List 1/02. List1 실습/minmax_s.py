import sys
sys.stdin = open('min_max.txt')

T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    temp = list(map(int, input().split()))
    for i in range(len(temp)-1, 0, -1):
        for j in range(0, i):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
    res = temp[len(temp)-1] - temp[0]
    print('#{} {}'.format(test_case, res))