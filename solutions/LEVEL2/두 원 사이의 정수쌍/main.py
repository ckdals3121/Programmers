# 1사분면의 점 개수를 구한 뒤 * 4 를 해 준다.
# 각 사분면의 점 개수는 모두 동일하기 때문이다

import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1) :
        temp = 0
        if i < r1 :
            temp = math.ceil(math.sqrt(r1 ** 2 - i ** 2))

        answer += int(math.sqrt(r2 ** 2 - i ** 2)) - temp + 1
        
    return answer * 4