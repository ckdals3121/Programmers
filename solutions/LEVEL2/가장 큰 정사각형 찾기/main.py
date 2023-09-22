# DP 를 활용하며, 위, 왼쪽, 왼쪽 대각선 위 숫자 중에서 가장 작은 수에 1을 더한 수로 업데이트 한다.
# DP를 활용하는 이유는, 정사각형을 작은 정사각형부터 시작해서 크기를 키워나갈 수 있기 때문이다

def solution(board):
    n = len(board)
    m = len(board[0])
    answer = 0
    
    for i in range(1, n) :
        for j in range(1, m) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1]) + 1
                
    for i in range(n) :
        answer = max(answer, max(board[i]))

    return answer ** 2