# Counter를 활용해서 크기: 개수 형태로 만든 후, 개수를 기준으로 내림차순으로 정렬한다.
# 개수가 많은 것부터 상자에 넣으며 카운트 한다

from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sort_ = sorted(counter.items(), key = lambda x : x[1], reverse = True)
    
    for cnt in sort_ :
        k -= cnt[1]
        answer += 1
        if k <= 0 :
            return answer
