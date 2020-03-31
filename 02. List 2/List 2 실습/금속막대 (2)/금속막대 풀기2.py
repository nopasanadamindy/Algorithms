import sys
sys.stdin = open('(1259)금속막대_input.txt')

T = int(input())
for i in range(1, 1+1):
    N = int(input())
    data = list(map(int, input().split()))

    Male = data[::2]
    Female = data[1::2]
    Result = [0] * (2*N)
    print(Male)
    print(Female)
    for idx in range(len(Male)):
        if Male[idx] not in Female:
            Start_idx = idx
            print(Start_idx)
    Result[0], Result[1] = Male[Start_idx], Female[Start_idx]

    I
    # dict = {}
    # for i in range(len(data)):
    #     if data[i] not in dict:
    #         dict[data[i]] = 1
    #     else:
    #         dict[data[i]] += 1
    # # print(dict)
    # for idx, cnt in dict.items():
    #     print(idx, cnt)