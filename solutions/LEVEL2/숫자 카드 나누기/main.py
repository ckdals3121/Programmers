# gcd를 구해서, 다른 어레이에 나눠지는 수가 있는지 모두 확인한다

import math

def canDivide(array, a):
    for i in range(len(array)):
        if array[i] % a == 0:
            return True
    return False

def solution(arrayA, arrayB):
    answer = 0
    
    if len(arrayA) == 1 :
        if arrayA[0] == arrayB[0] :
            return 0
        else :
            return max(arrayA[0], arrayB[0])
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for i in range(1, len(arrayA)) :
        gcdA = math.gcd(gcdA, arrayA[i])
        gcdB = math.gcd(gcdB, arrayB[i])
    
    if gcdA != 1 and not canDivide(arrayB, gcdA) :
        answer = max(answer, gcdA)
    if gcdB != 1 and not canDivide(arrayA, gcdB) :
        answer = max(answer, gcdB)
    
    
    return answer