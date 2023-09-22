# 우선 2번째 컨베이어 벨트로 다 보내버리고, 그 다음에 숫자가 맞는 것이 나오면 다 pop 한다

def solution(order):
    second = []
    cnt = 0 
    
    for i in range(1, len(order) + 1) :
        second.append(i)
        while second and second[-1] == order[cnt] :
            cnt += 1
            second.pop()

    return cnt