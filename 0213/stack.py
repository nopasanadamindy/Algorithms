### 1. C 언어
SIZE = 100
stack = [0] * SIZE
top = -1

def push(item):
    global top # 값형은 원래 read only인데 write 가능하게 하기 위해
    if top > SIZE -1: # full 인지 아닌지 판단(가득 차면 안된다/SIZE보다 크면 안된다) Q. -1?????이렇게 해도 됨??
        return #False
    else:
        top += 1 # top을 먼저 올려주고
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('stack is empty!')
        return 0; # 아무것도 도출하지 않겠다. or False
    else:
        result = stack[top]
        top -= 1
        return result

push(1)
push(2)
push(3)

item = pop()
print('pop item => %d' % item)
item = pop()
print('pop item => %d' % item)
item = pop()
print('pop item => %d' % item)


### 2. 파이썬

stack = []
stack.append(1)
stack.append(2)
stack.append(3)


if stack: #****스택이 비지 않았다는 것을 체크하는 것이 너모 중요해
    stack.pop()
if stack:
    stack.pop()
if stack:
    stack.pop()
if stack:
    stack.pop()

[문제 : 괄호체크]
s = list()
def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            s.append(data[i])
        elif data[i] == ')': #만약 괄호의 종류가 많다면 요 구문이 많아야한다
            if len(s) == 0:
                return False
            else:
                s.pop()

    if s: return False
    else: return True

data = input()
print(check_matching(data))


[문제 : 팩토리알 재귀 구현]

def Factorial(n):
    if n == 1: # basis part 멈추는 파트(1or2개)
        return 1
    else:
        return n * fact(n - 1) # inductive 유도파트(재귀식) #else가 왜 필요없징


print(factorial(4))

[문제 : 피보나치 재귀 구현]
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
print(fibo(8))


### 3. Memoization : O(n)
#1) recursive 방식 : 비효율적
def fibo1(n):
    # global memo 굳이 ㄴㄴ
    if n >= 2 and len(memo) <= n: 안구해져 있따면
        memo.append(fibo1(n -1) + fibo1(n - 2))
    return memo[n]
memo = [0, 1]
print(fibo(50))

#2) iterative 방식 : 보다 효율적
[DP피보나치 적용 알고리즘] # 호출을 하지 않아도 되어서 훨씬 빠르다능~.~(DP가 빠르다)
def fibo2(n):
    f = [0, 1]

    for i in ragne(2, n + 1):
        f.append(f[i - 1] + f[i - 2]) # 점화식

    return f[n]