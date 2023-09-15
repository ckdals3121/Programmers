# 각각의 progress 가 종료되는데 걸리는 일 수 들을 넣어둔 end_date 리스트를 만든다
# 첫번째 progress 가 종료되는데 걸리는 일 수 로 end_date 값들을 모두 빼준다.
# 걸리는 일 수가 0 이하가 된 것들은 모두 한번에 실행 완료가 되는 것이다

import math

def solution(progresses, speeds):
    answer = []
    end_date = []
    
    for i in range(len(progresses)) :
        end_date.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    idx = 0    
    while idx < len(progresses) :
        temp = end_date[idx]
        end_date = [x - temp for x in end_date]
        print(end_date)
        cnt = 0
        while idx < len(progresses) and end_date[idx] <= 0 :
            cnt += 1
            idx += 1
        answer.append(cnt)
    return answer