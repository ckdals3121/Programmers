# visited 배열을 만들어서 모든 곳을 순회하면서, X가 아니면서 방문하지 않은 곳이 나오면, 주변에 연결된 장소들을 다 순회하면서 값을 더한다. 한 구역을 다 순회하면, 그 구역은 모두 visited가 되므로 더이상 그 구역은 안들어가게 된다

def solution(maps):
    answer = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    col = len(maps)
    row = len(maps[0])
    
    visited = [[False] * row for _ in range(col)]
    
    for i in range(col) :
        for j in range(row) :
            if maps[i][j] != "X" and not visited[i][j] :
                period = 0
                pos = [(j, i)]
                
                while len(pos) != 0 :
                    x, y = pos.pop()
                    if not visited[y][x] :
                        visited[y][x] = True
                        period += int(maps[y][x])
                        
                        for k in range(4) :
                            px, py = x + dx[k], y + dy[k]
                            if -1 < px < row and -1 < py < col and maps[py][px] != "X" and not visited[py][px] :
                                pos.append((px, py))
                    
                answer.append(period)
    
    if len(answer) == 0 :
        return [-1]
    
    return sorted(answer)