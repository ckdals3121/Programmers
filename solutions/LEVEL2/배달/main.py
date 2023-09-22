# dijkstra 알고리즘을 활용해서 k 보다 거리가 짧은 곳들을 골라낸다

import heapq

def dijkstra(roads, start, distance) :
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist :
            continue
        
        for road in roads :
            if road[0] == now :
                cost = dist + road[2]
                if cost < distance[road[1]] :
                    distance[road[1]] = cost
                    heapq.heappush(q, (cost, road[1]))
            elif road[1] == now :
                cost = dist + road[2]
                if cost < distance[road[0]] :
                    distance[road[0]] = cost
                    heapq.heappush(q, (cost, road[0]))
    
    return distance
        

def solution(N, road, K):
    answer = 0

    dists = dijkstra(road, 1, [int(1e9) for _ in range(N + 1)])
    
    answer = [i for i in dists if i <= K]
    
    return len(answer)