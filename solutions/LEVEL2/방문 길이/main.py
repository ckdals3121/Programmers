# 4차원 배열을 선언해서, 해당 구간을 이미 지났는지 처음 지났는지 확인한다

def solution(dirs):
    answer = 0
    is_visited = [[[[0 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

    
    directions = {"U": [1, 0], "D": [-1, 0], "R": [0, 1], "L": [0, -1]} 
    
    x = y = 5
    
    for i in range(len(dirs)) :
        if 0 <= x + directions[dirs[i]][0] < 11 and 0 <= y + directions[dirs[i]][1] < 11 :
            if is_visited[x][y][x + directions[dirs[i]][0]][y + directions[dirs[i]][1]] == 0 :
                is_visited[x][y][x + directions[dirs[i]][0]][y + directions[dirs[i]][1]] = 1
                is_visited[x + directions[dirs[i]][0]][y + directions[dirs[i]][1]][x][y] = 1
                answer += 1
            x += directions[dirs[i]][0]
            y += directions[dirs[i]][1]
            
    
    return answer

print(solution("ULURRDLLU"))