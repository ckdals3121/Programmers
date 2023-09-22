# 3진수 만드는 방법과 비슷하다. 하지만 자리수가 3의 배수일 때는 주의해야 한다

def solution(n):
    answer = ''
    numbers = ['4', '1', '2']
    while n != 0 :
        mod = n % 3
        n = n // 3
        
        if mod == 0 :
            n -= 1
        
        answer += numbers[mod]
        
    return answer[::-1]