# 2차원 배열에서 [x][y] 의 값은 max(x, y) + 1 이다
# 2차원 배열을 1차원 배열로 만들었을 때 [x] 의 값은 max(x // n, x % n) + 1 이다.
# x // n 이 원래의 x값, x % n 이 원래의 y값 이다

def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
        
    return answer