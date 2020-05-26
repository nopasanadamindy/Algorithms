def solution(n):
    answer = ''
    while len(answer) < n:
        answer += '수박'
    return answer[0:n]
print(solution(3))