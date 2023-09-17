# 참고 [https://my-coding-notes.tistory.com/226]
# 완전탐색이다.

def solution(m, n, board):
    for i in range(m) :
        board[i] = list(board[i])
        
    cnt = 0
    rm_pos = set()
    
    while True :
    
        for i in range(m - 1) :
            for j in range(n - 1) :
                if board[i][j] != [] :
                    temp = board[i][j]
                    if board[i + 1][j] == temp and board[i + 1][j + 1] == temp and board[i][j + 1] == temp :
                        rm_pos.add((i, j))
                        rm_pos.add((i + 1, j))
                        rm_pos.add((i + 1, j + 1))
                        rm_pos.add((i, j + 1))

        if len(rm_pos) != 0 :
            cnt += len(rm_pos)
            for pos in rm_pos :
                board[pos[0]][pos[1]] = []
            rm_pos = set()
        else :
            return cnt

        while True :
            moved = 0
            for i in range(m - 1) :
                for j in range(n) :
                    if board[i][j] != [] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0 :
                break
