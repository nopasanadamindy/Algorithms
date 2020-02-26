def Solve(data, Cnt):
    Max_Idx = 0
    Min_Idx = 0
    for i in range(Cnt):
        for j in range(len(data)):
            if data[j] >= data[Max_Idx]:
                Max_Idx = j
            if data[j] <= data[Min_Idx]:
                Min_Idx = j
        data[Max_Idx] -= 1
        data[Min_Idx] += 1

    Max_height = data[0]
    Min_height = data[0]
    for r in range(len(data)):
        if data[r] >= Max_height:
            Max_height = data[r]
        if data[r] <= Min_height:
            Min_height = data[r]
    return Max_height - Min_height

import sys
sys.stdin = open('(1208)Flatten_input.txt')

T = 10
for test_case in range(1, T+1):
    Cnt = int(input())
    data = list(map(int, input().split()))
    print('#{} {}'.format(test_case, Solve(data, Cnt)))