

def CheckMatching(data):
    for i in len(data):
        if data[i] == '(':
            s.append(data[i])
        if data[i] == '{':
            m.append(data[i])
        if data[i] == '[':
            b.append(data[i])
        if data[i] == ')':
            if s:
                s.pop()
        if data[i] == '}':
            if m:
                m.pop()
        if data[i] == ']':
            if b:
                b.pop()
    if s == True and m == True and b == True:
        return 0
    else:
        return 1



T = int(input()))

for test_case in data(1, T + 1):


s =[]
m =[]
b =[]