# number를 n진수로 변경하는 함수 convert 를 작성한다
# 불리는 숫자들을 모두 구해둔 후, 튜브가 외치는 숫자를 찾아서 append 한다

def convert(number, n) : 
    if number == 0 :
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0 :
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]

def solution(n, t, m, p) :
    answer = ''
    game = ''
    cur = p - 1
    
    for num in range(t * m) :
        game += convert(num, n)
        
    while 1 :
        if len(answer) == t :
            break
        answer += game[cur]
        cur += m
        
    return answer