import sys
sys.stdin =open("data.txt")

# 성묵코드
for tc in range(1, int(input())+1):
    busstop = [0] * 5001
    result = []
    for _ in range(int(input())):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busstop[i] += 1
        for _ in range(int(input())):
            result.append(busstop[int(input())])
        print('#{0}'.format(tc), *result)