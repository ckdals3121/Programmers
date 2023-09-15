# discount 를 10개씩 자른 후, 할인행사 상품: 횟수 형식으로 counter를 만든다.
# want 용량만큼 counter에 있는지 확인한다

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9) :
        counter = Counter(discount[i: i + 10])
        if all(counter[want[j]] >= number[j] for j in range(len(want))) :
            answer += 1
    return answer