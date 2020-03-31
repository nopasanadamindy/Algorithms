import sys
sys.stdin =open("data.txt")

# 세진코드
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    result = []
    print(bus)
    for _ in range(P):
        C = int(input())
        cnt = 0
        for A, B in bus:
            if A <= C <= B:
                cnt += 1
        result.append(cnt)
    print('#{}'.format(test_case), *result)