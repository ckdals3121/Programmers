# 모든 wires 를 순회하면서, 하나씩 없애고 dfs 를 돌린다

def dfs(start, visit) :
    global cnt, tree
    visit.append(start)
    cnt += 1
    for i in tree[start] :
        if i not in visit :
            dfs(i, visit)

def solution(n, wires):
    answer = n
    global tree, cnt
    tree = [[] for _ in range(n + 1)]
    
    for x, y in wires :
        tree[x].append(y)
        tree[y].append(x)
        
    for x, y in wires :
        tree[x].remove(y)
        tree[y].remove(x)
        
        cnt = 0
        dfs(1, [])
        answer = min(answer, abs(cnt - (n - cnt)))
        
        tree[x].append(y)
        tree[y].append(x)
        
    return answer