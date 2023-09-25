# combination 으로 모든 조합을 구하고 유일성과 최소성을 조사한다

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    combis = []
    
    for i in range(1, col + 1) :
        combis += list(combinations(range(col), i))
        
    unique = []
    
    for combi in combis :
        temp = [tuple(item[i] for i in combi) for item in relation]
        if len(set(temp)) == row :
            for x in unique :
                if set(x).issubset(set(combi)) :
                    break
            else :
                unique.append(combi)

    return len(unique)