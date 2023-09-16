# 제일 안매운 것과 두번째로 안매운 것을 섞어서 다시 넣는 것을 반복한다

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        temp = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, temp)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K :
            return -1
    return answer