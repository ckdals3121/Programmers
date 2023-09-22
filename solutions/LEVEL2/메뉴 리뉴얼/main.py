# combinations 로 모든 경우의 수를 다 구하고, Counter 를 활용해서 2번 이상 나온 것들을 담는다

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for cours in course :
        temp = []
        
        for order in orders :
            temp += list(combinations(sorted(order), cours))
        
        counter = Counter(temp)
        
        if len(counter) != 0 and max(counter.values()) > 1 :
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    
    return sorted(answer)