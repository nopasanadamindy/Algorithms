import sys
sys.stdin = open('(1221)GNS_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = input()
    data = list(map(str, input().split()))
    dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for i in range(len(data)):
        if data[i] in dict:
            dict[data[i]] += 1
    # print(dict)
    print('#{}'.format(test_case))
    for key, cnt in dict.items():
        print((key + ' ') * cnt)
    print()
    # for i in range(10):
    #     for j in range()
    # print('#{}'.format(test_case))
    # print(' '.join(result))
    # for i in range(len(result)):
    #     print(result[i], end = ' ')
    # print()


# 도자기코드 ♥
    # T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    # for test_case in range(1, T + 1):
    #     length = input()
    #     data = list(input().split())
    #     arr = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    #     brr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    #     for i in data:
    #         arr[i] += 1
    #     print('#{}'.format(test_case))
    #     for i in range(10):
    #         for j in range(arr[brr[i]]):
    #             print(brr[i], end=' ')