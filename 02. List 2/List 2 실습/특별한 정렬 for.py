def sorting(a):#선택정렬
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                a[min], a[j] = a[j], a[min]
import sys
sys.stdin = open('특별한정렬_input.txt')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    data = list(map(int, input().split()))
    # print(data)
    sorting(data)

    result = []
    for x in range((len(data))//2-1):
        result.append(data[len(data)-1 - x])
        result.append(data[x])
    print(result)

    # print('#{}'.format(test_case), end = ' ')
    # for i in range(10):
    #     print(result[i], end = ' ')
    # print()