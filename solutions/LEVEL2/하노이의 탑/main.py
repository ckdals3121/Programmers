# hanoi 탑을 푸는 법은, (n - 1) 개를 한 곳으로 옮기고, n 번째를 다른 곳으로 옮기고, (n - 1)개를 다시 n번째를 옮긴 곳으로 옮기는 것이다.
# 그렇기 때문에 재귀로 풀 수있다

def hanoi(num, start, end) :
    if num == 1:
        return [[start, end]]

    another = 0
    for i in range(1, 4) :
        if i != start and i != end:
            another = i
            break
        
    return hanoi(num - 1, start, another) + [[start, end]] + hanoi(num - 1, another, end)

def solution(n):
    return hanoi(n, 1, 3)