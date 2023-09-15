# 초기 사전 dic을 만든다
# msg 를 순회하면서 조건에 맞게 연산을 수행한다

def solution(msg):
    answer = []

    dic = {chr(i + 64): i for i in range(1, 27)}

    w = c = 0 
    while True :
        c += 1	
        if c == len(msg) :	
            answer.append((dic[msg[w : c]]))
            break

        if msg[w : c + 1] not in dic :
            dic[msg[w : c + 1]] = len(dic) + 1
            answer.append(dic[msg[w : c]])
            w = c	
            
    return answer