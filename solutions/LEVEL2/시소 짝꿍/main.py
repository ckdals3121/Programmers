# Counter와 set를 활용해서 1:1, 2:3, 2:4, 3:4 의 경우를 더해준다

from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    for k, v in counter.items() :
        if v > 1 :
            answer += v * (v - 1) // 2
    
    weights = set(weights)
    
    for w in weights :
        if w * 2 / 3 in weights :
            answer += counter[w * 2 / 3] * counter[w]
        if w * 2 / 4 in weights :
            answer += counter[w * 2 / 4] * counter[w]
        if w * 3 / 4 in weights :
            answer += counter[w * 3 / 4] * counter[w]
    return answer