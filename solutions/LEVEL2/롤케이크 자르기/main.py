# 내가 전부 가지고 있는 것 부터 시작해서, 동생에게 하나씩 주는 상황을 연출한다

from collections import Counter

def solution(topping):
    answer = 0
    mine = Counter(topping) 
    bros = {}
    
    for i in range(len(topping)) :
        if topping[i] in bros :
            bros[topping[i]] += 1
        else :
            bros[topping[i]] = 1
        
        mine[topping[i]] -= 1
        
        if mine[topping[i]] == 0 :
            del mine[topping[i]]
        
        if len(mine) == len(bros) :
            answer += 1

    return answer