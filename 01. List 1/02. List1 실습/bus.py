import sys
sys.stdin = open('bus.txt')

def Move(stop):
    global cnt, K, N
    if stop >= N:
        return cnt
    else:
        for i in range(stop, len(bus), K): #이동
            if bus[i] != 1: #그 곳에 충전기가 X
                for j in range(i-1, i-K, -1):
                    if bus[j] == 1:
                        cnt += 1
                        stop = bus[j]
                        Move(stop)
            else: #그 곳에 충전기가 O
                cnt += 1
                stop = bus[i]
                Move(stop)

T = int(input())
for test_case in range(1, 1+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    bus = [0 for _ in range(N+1)]
    cnt = 0
    # 버스정류장 표시
    for i in range(len(data)):
        bus[data[i]] = 1
    Move(0)