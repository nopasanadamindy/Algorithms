d = [2,2,3,3]
budget = 10

def solution(d, budget):
    d = sorted(d)
    hap = 0
    temp = []
    for i in range(len(d)):
        hap += d[i]
        temp.append(hap)
    ans = []
    for j in range(len(temp)):
        if temp[j] <= budget:
            ans.append(temp[j])
    return len(ans)


print(solution(d, budget))