import sys
sys.stdin =open("data.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = [0 for _ in range(5001)]
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            result[j] += 1
    # print(result)

    P = int(input())
    print('#{}'.format(test_case), end = ' ')
    for i in range(P):
        C = int(input())
        ans = result[C]
        print(ans, end = ' ')
    print()