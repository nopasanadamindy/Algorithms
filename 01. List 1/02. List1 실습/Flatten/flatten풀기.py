import sys
sys.stdin = open('(1208)Flatten_input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # Max, Min 찾아서 Flatten하기
    for j in range(N):
        Max_idx = 0
        Min_idx = 0
        for i in range(len(data)):
            if data[i] >= data[Max_idx]:
                Max_idx = i
            if data[i] <= data[Min_idx]:
                Min_idx = i
        data[Max_idx] -= 1
        data[Min_idx] += 1

    # 차이 구하기
    Max_res = data[0]
    Min_res = data[0]
    result = 0
    for r in range(len(data)):
        if data[r] > Max_res:
            Max_res = data[r]
        if data[r] < Min_res:
            Min_res = data[r]
    result = Max_res - Min_res
    print('#{} {}'.format(test_case, result))