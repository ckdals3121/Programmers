# 완전탐색으로 사전을 생성한다

from itertools import product

def solution(word):
    words = []
    
    for i in range(1, 6) :
        for temp in product(['A', 'E', 'I', 'O', 'U'], repeat = i) :
            words.append(''.join(list(temp)))
    words.sort()
    
    return words.index(word) + 1
