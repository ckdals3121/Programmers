# x * y = brown + yellow
# (x - 2) * (y - 2) = yellow
# 두 식을 활용해서 2차 방정식을 풀면, 
# x^2 - (brown / 2 + 2)x + brown + yellow = 0
# 의 두 근이 가로와 세로의 길이

import math

def solution(brown, yellow):
    a = 1
    b = - (brown / 2 + 2)
    c = brown + yellow
    
    D = b ** 2 - 4 * a * c
    
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    
    answer = []
    answer.append(x1)
    answer.append(x2)
    
    return answer