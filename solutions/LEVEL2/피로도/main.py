# DFS 를 돌면서, 피로도가 음수가 되기 전까지 몇개의 던전을 도는지 확인한다.

global answer
answer = 0

def DFS(k, cnt, dungeons, check) :
    global answer
    
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)) :
        if check[i] == 0 and dungeons[i][0] <= k :
            check[i] = 1
            DFS(k - dungeons[i][1], cnt + 1, dungeons, check)
            # DFS 를 돌고난 다음에는 다시 가지 않은 것으로 처리해줘야 한다
            check[i] = 0

def solution(k, dungeons):
    global answer
    
    check = [0 for _ in range(len(dungeons))]
    
    DFS(k, 0, dungeons, check)
    
    
    return answer