
import sys
sys. stdin = open('0204.txt.txt')

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    data = list(map(int, input().split()))
    # print(data)

result1 = [] # 짝수인덱스
result2 = [] # 홀수인덱스
result3 = []
#1. idx값 짝/홀 나눠서 리스트에 넣어주기
for i in range(len(data)):
    if i % 2 == 0:
        result1.append(data[i])
    else:
        result2.append(data[i])
# print(result1)
# print(result2)

#2. 같은 값이 있는지 찾아주기(시작값을 찾기 위해) if ~~
for x in result1:
    if x not in result2:




# print()




# for i in range(len(data)):
#     if i % 2 == 0
#         result.append()
#
#     if result[1] == data[i % 2 == 0]:
#         result.append()

