# queue 에는 process 의 인덱스 값들이 들어가 있다.
# 우선순위가 가장 높은 process 가 뽑혔다면, 실행을 시키고, 해당 process 의 priority를 0으로 업데이트한다

from queue import Queue

def solution(priorities, location):
    answer = 0
    
    q = Queue()
    
    for i in range(len(priorities)) :
        q.put(i)
    
    while True :
        process = q.get()
        if priorities[process] == max(priorities) :
            answer += 1
            priorities[process] = 0
            if process == location :
                return answer
        else :
            q.put(process)
            