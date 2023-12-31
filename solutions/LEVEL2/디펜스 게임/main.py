# heap 을 사용해서 처음 k개를 넣어주고, k개 이후부터는 넣고 빼서 n에서 빼준다

import heapq

def solution(n, k, enemy) :
    stage = len(enemy)

    if k >= stage :
        return stage
    
    q = []

    for i in range(stage) :
        heapq.heappush(q, enemy[i])
        if len(q) > k :
            last = heapq.heappop(q)
            if last > n :
                return i
            n -= last
    
    return stage