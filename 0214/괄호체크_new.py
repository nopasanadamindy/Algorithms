
def check(data):
    s = [] # 호출할 떄마다 초기화해야되니까
    for i in data:
        if i == '(' or i == '{':
            s.append(i)
        elif i == ')' or i == '}':
            if data[-1] == i:
                s.pop()
            else:
                return 0
    if s:
        return 0
    else:
        return 1

import sys
sys.stdin = open()

T = int(input())
for test_case in range(T):
    data = input()

    print(check(data))