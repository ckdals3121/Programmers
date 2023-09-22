# 각 자리수 마다 나눗셈 연산을 활용해서 수를 바꿔준다

from math import factorial

def solution(n, k):
    answer = []
    k -= 1
    remain = [i for i in range(1, n + 1)]
    
    for i in range(n, 0, -1) :
        div, k = divmod(k, factorial(i - 1))
        answer.append(remain.pop(div))
    return answer