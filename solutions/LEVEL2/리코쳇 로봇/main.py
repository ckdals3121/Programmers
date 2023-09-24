# BFS 를 수행하며, 미끄러지는 것이 한번 이동인 것을 주의한다

from collections import deque

def solution(board) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(board)
    m = len(board[0])
    q = deque()
    dist = [[int(1e9)] * m for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'R' :
                q.append((i, j, 0))
                dist[i][j] = 0
        
        if q :
            break
    
    while q :
        x, y, cnt = q.popleft()

        if board[x][y] == 'G' :
            return cnt
        
        for i in range(4) :
            nx = x
            ny = y

            while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m and board[nx + dx[i]][ny + dy[i]] != 'D' :
                nx += dx[i]
                ny += dy[i]
            
            if dist[nx][ny] > cnt + 1 :
                dist[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))
            
    return -1

