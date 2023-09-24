# 시작지점부터 레버지점까지 BFS 1번, 래버지점부터 끝지점가지 BFS 1번 총 2번 수행해주면 된다

from collections import deque

def BFS(start, end, maps) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == start :
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag :
            break
    
    while q :
        y, x, cnt = q.popleft()

        if maps[y][x] == end :
            return cnt
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X' and not visited[ny][nx] :
                q.append((ny, nx, cnt + 1))
                visited[ny][nx] = True
    
    return -1

def solution(maps) :
    path1 = BFS('S', 'L', maps)
    path2 = BFS('L', 'E', maps)

    if path1 != -1 and path2 != -1 :
        return path1 + path2
    
    return -1
