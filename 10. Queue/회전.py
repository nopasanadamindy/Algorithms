import sys
sys.stdin = open('회전.txt')
from _collections import deque
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     # print(data)
#     for i in range(M):
#         a = data.pop(0)
#         data.append(a)
#     print('#{} {}'.format(test_case,data[0]))

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)
    # queue에 넣기
    que = deque()
    for i in range(N):
        que.append(data[i])
    # 회전하기
    for j in range(M):
        a = que.popleft()
        que.append(a)
    print('#{} {}'.format(test_case, que[0]))