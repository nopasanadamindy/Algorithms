def Binary(start, end, key):
    global cnt
    if start >= end:
        return False
    cnt += 1
    else:
        middle = (start + end) // 2
        if key == middle:
            return cnt
        elif key < middle:
            Binary(star  t, middle, key)
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
    print(Binary(1, P, Pb))