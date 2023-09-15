# n + 1 부터 완전탐색 하면서 2진수로 변경했을 때 1의 개수가 같은 수를 찾음

def solution(n):
    answer = n + 1
    
    while True :
        if format(n, 'b').count('1') == format(answer, 'b').count('1') :
            return answer
        else :
            answer += 1