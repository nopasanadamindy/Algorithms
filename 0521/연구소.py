import sys
sys.stdin = open('연구소.txt')

def prin(a):
    for i in range(len(a)):
        print(*a[i])

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    print(N, M)
    # G = [[0 for _ in range(M)] for _ in range(N)]
    result = []
    for i in range(N):
        temp = list(map(int, input().split()))
        result.append(temp)
    print(result)
