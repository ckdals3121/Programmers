# 각각 합을 구해서 더 큰쪽의 queue 에서 같을 하나 빼서 다른 쪽으로 넣어주는 것을 반복한다

from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    sumtotal = sum1 + sum2
    
    if sumtotal % 2 != 0 :
        return -1
    
    limit = 4 * len(queue1)
    
    while answer <= limit :
        if sum1 > sum2 :
            temp = q1.popleft()
            q2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum1 < sum2 :
            temp = q2.popleft()
            q1.append(temp)
            sum1 += temp
            sum2 -= temp
        else :
            return answer
        answer += 1
    
    return -1