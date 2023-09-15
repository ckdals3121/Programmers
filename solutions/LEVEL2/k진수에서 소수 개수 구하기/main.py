# 소수인지 확인하는 isprime 함수를 만든다.
# n을 k진수 수로 표현한 후 투포인트로 부분 문자열들을 다 찾아서 조건에 맞는지 확인한다

def isprime(n) :
    if n == 1 :
        return False
    
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    
    return True

def solution(n, k):
    answer = 0
    
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    kth = rev_base[::-1] 
    
    for i in range(len(kth)) :
        for j in range(i, len(kth)) :
            temp_P = kth[i: j + 1]
            if isprime(int(temp_P)) :
                if '0' not in temp_P :
                    if i == 0 and j == len(kth) - 1 :
                        answer += 1
                    elif i == 0 and kth[j + 1] == '0' :
                        answer += 1
                    elif j == len(kth) - 1 and kth[i - 1] == '0' :
                        answer += 1
                    elif kth[i - 1] == '0' and kth[j + 1] == '0' :
                        answer += 1
    
    return answer