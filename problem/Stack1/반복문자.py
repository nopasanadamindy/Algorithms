import sys
sys.stdin = open('반복문자.txt')


T = int(input())
for tc in range(1, T + 1):
    data = input()
    # print(data)
    stack = []
    for i in range(len(data)):
        if len(stack) == 0:
            stack.append(data[i])
        elif stack[-1] == data[i]:
            stack.pop()
        else:
            stack.append(data[i])

    print('#{} {}'.format(tc, len(stack)))


def Stack(data):
    # stack = [] # 함수안에 list를 두고 return하면 위험하다..전역으로 바꿔줘야해
    for i in range(len(data)):
        if len(stack) == 0:
            stack.append(data[i])
        elif data[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(data[i])
    # return stack # 이렇게 하면 안됨. 위험함


T = int(input())
for tc in range(1, T + 1):
    data = input()
    stack = [] # 전역으로 stack을 빼줌
    Stack(data)
    print('#{} {}'.format(tc, len(stack)))