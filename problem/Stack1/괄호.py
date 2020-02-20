import sys
sys.stdin = open('괄호.txt')


def Check(data):
    result = []
    for i in range(len(data)):
        # 만약 (나 {가 나오면 무조건 result.append()
        if data[i] == '(' or data[i] == '{':
            result.append(data[i])
        # 만약 )나 }가 나온다면 꺼내기
        elif data[i] == ')' or data[i] == '}':
            # 만약 result가 비어있다면 그만하기
            if len(result) == 0:
                return 0
            # 그렇지 않다면 같은 쌍이 아니라면
            elif (data[i] == ')' and result[-1] !='('): ######
                return 0
            elif (data[i] == '}' and result[-1] != '{'): ######
                return 0
            # 같은 쌍이라면 pop해라
            else:
                result.pop()
    if len(result) != 0:
        return 0
    else:
        return 1

T = int(input())

for test_case in range(1, T + 1):
    data = input()

    print('#{} {}'.format(test_case, Check(data)))



# def Check(data):
#     result = []
#     for i in range(len(data)):
#         # 만약 (나 {가 나오면 무조건 result.append()
#         if data[i] == '(' or data[i] == '{':
#             result.append(data[i])
#         # 만약 )나 }가 나온다면 꺼내기
#         elif data[i] == ')' or data[i] == '}':
#             # 만약 result가 비어있다면 그만하기
#             if len(result) == 0:
#                 return 0
#             # 그렇지 않다면 같은 쌍이 아니라면
#             elif not (data[i] == ')' and result[-1] =='('): #####
#                 return 0
#             elif not (data[i] == '}' and result[-1] == '{'): ######
#                 return 0
#             # 같은 쌍이라면 pop해라x
#             else:
#                 result.pop()
#     if len(result) != 0:
#         return 0
#     else:
#         return 1
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     data = input()
#
#     print('#{} {}'.format(test_case, Check(data)))
