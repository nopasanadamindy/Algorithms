s = 'try hello world'

def solution(s):
    temp = s.split()
    data = []
    for i in range(len(temp)):
        answer = ''
        for j in range(len(temp[i])):
            if j % 2 == 0:
                big = temp[i][j].upper()
                answer += big
            else:
                small = temp[i][j].lower()
                answer += small
        data.append(answer)
    ans = ' '.join(data)
    return ans

print(solution(s))