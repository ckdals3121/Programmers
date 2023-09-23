# x를 기준으로 y의 최대값을 구해서, answer 에 값을 계속 더해준다

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k) :
        temp = int((d ** 2 - x ** 2) ** 0.5)
        answer += temp // k + 1
    return answer