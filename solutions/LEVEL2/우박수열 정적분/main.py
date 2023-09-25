# 0부터 a 까지의 정적분을 구한다.
# a 부터 b까지의 정적분은 0부터 b까지의 정적분 - 0부터 a까지의 정적분이다

def solution(k, ranges):
    answer = []
    integral0toI = [0.0]

    while k != 1 :
        newK = (k // 2) if k % 2 == 0 else (3 * k + 1)
        integral0toI.append(integral0toI[-1] + (k + newK) * 0.5)
        k = newK
    
    n = len(integral0toI)

    for r in ranges :
        if n - 1 + r[1] >= r[0] :
            answer.append(integral0toI[r[1] - 1] - integral0toI[r[0]])
        else :
            answer.append(-1)
    return answer