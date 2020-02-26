def binary(P, key):
    s = 1
    e = P
    cnt = 0
    while s <= e:
        cnt += 1
        m = (s + e) // 2
        if key == m:
            return cnt
        elif key < m:
            e = m
        else:
            s = m
    return cnt

def PrintSet(a, b):
    if a < b:
        return 'A'
    elif b < a:
        return 'B'
    else:
        return 0

import sys
sys.stdin = open('이진탐색_input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    print('#{} {}'.format(test_case, PrintSet(binary(P, Pa), binary(P, Pb))))