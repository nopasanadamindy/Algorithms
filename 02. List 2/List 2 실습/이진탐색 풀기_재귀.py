def Binary(start, end, key):
    global cnt
    cnt += 1
    if start >= end:
        return False
    else:
        middle = (start + end) // 2
        if key == middle:
            return cnt
        elif key < middle:
            Binary(start, middle, key)
        else:
            Binary(middle, end, key)
    return cnt

import sys
sys.stdin = open('이진탐색_input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt = 0
    print(Binary(1, P, Pa))
    cnt = 0### 초기화시켜줘야해
    print(Binary(1, P, Pb))

