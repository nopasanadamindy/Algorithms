import sys
sys.stdin = open('(1206)View_input.txt')

T = 10
for test_case in range(1, 1 + T):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(2, len(data)-2):
        max_height = data[0]
        second_height = data[0]
        for j in range(i-2, i+2+1):
            if data[j] >= max_height:
                max_height = data[j]
            if j != i:
                if data[j] >= second_height:
                    second_height = data[j]
        result += max_height - second_height
    print('#{} {}'.format(test_case, result))
