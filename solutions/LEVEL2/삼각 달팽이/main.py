# 아래로, 오른쪽으로, 왼쪽 대각선으로 를 순서대로 방향을 바꾸기 때문에, 그렇게 진행한다

def solution(n):
    snail = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n) :
        for j in range(i, n) :
            if i % 3 == 0:     
                x += 1          
            elif i % 3 == 1:    
                y += 1            
            elif i % 3 == 2:   
                x -= 1
                y -= 1     
                
            snail[x][y] = num
            num += 1
            
    for i in range(n):
        for j in range(n):
            if snail[i][j] != 0 :
                answer.append(snail[i][j])
    return answer