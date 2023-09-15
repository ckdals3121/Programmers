# str1, str2 를 2글자씩 끊어서 2글자가 모두 알파벳이면, 소문자로 append 를 한다.
# 그런 다음 2글자: 개수 형태로 Counter(multiset) 을 만든 후, intersection 연산과 union 연산을 수행한다

from collections import Counter
import math

def solution(str1, str2):
    set1 = []
    set2 = []
    
    for i in range(len(str1) - 1) :
        if str1[i].isalpha() and str1[i + 1].isalpha() :
            set1.append(str1[i: i + 2].lower())
    
    for i in range(len(str2) - 1) :
        if str2[i].isalpha() and str2[i + 1].isalpha() :
            set2.append(str2[i: i + 2].lower())
    
    if len(set1) == 0 and len(set2) == 0 :
        return 65536
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    intersection = sum(dict(counter1 & counter2).values())
    union = sum(dict(counter1 | counter2).values())
    
    answer = math.trunc(intersection / union * 65536)
    
    return answer