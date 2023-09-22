# 사람이 있는 곳을 모두 순회하면서, 각각의 응시생들이 거리두기를 만족하는지 확인한다

def ifValid(place):
    pList = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']

    for y, x in pList :
        for y2, x2 in pList :
            dist = abs(y - y2) + abs(x - x2) 
            if dist == 0 or dist > 2 :
                continue
            if dist == 1 :  
                return 0
            elif y == y2 and place[y][int((x + x2) / 2)] != 'X' :   
                return 0
            elif x == x2 and place[int((y + y2) / 2)][x] != 'X' :  
                return 0
            elif y != y2 and x != x2 : 
                if place[y2][x] != 'X' or place[y][x2] != 'X' :
                    return 0
    return 1

def solution(places) :
    answer = []

    for place in places :
        answer.append(ifValid(place))
        
    return answer
