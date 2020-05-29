# s = 'abcde'
s = 'qwer'

def solution(s):
    length = len(s)
    answer = ''
    if length % 2 == 1: # 홀수라면
        middle = length // 2
        answer += s[middle]
    else:
        middle = length // 2
        answer += s[middle-1]
        answer += s[middle]

    return answer

print(solution(s))